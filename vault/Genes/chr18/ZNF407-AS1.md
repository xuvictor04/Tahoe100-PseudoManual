---
symbol: "ZNF407-AS1"
type: "gene"
col: 15435
ensembl_id: "ENSG00000264247"
name: "ZNF407 antisense RNA 1"
location: "18q22.3"
module: 10
arm: "+"
pooled_cpm: 7.33
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ZNF407-AS1

*ZNF407 antisense RNA 1* — 18q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +10.5, q 7e-23, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.519× (z -6.9, q 3e-09, down in 24 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.536× (z -6.5, q 2e-08, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM200A]] (+0.85, fdr 7e-06), [[ATE1OSP]] (+0.81, fdr 7e-06), [[PCNX4-DT]] (+0.80, fdr 1e-05); moves opposite to [[FAM118A]] (-0.69, fdr 3e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NRIP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZEB1-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +10.5 | 7e-23 | 36/45 (BT-474, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +8.7 | 7e-16 | 35/43 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +8.7 | 7e-16 | 17/19 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +7.8 | 1e-12 | 29/45 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +7.3 | 2e-11 | 27/47 (PANC-1, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +5.4 | 8e-06 | 23/46 (SHP-77, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.8 | 1e-04 | 17/28 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.004 | 19/40 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.024 | 13/46 (SHP-77, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.3 | 0.046 | 12/34 (SW1417, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.61×** | +3.2 | 0.066 | 2/45 (NCI-H23, NCI-H460) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.078 | 12/46 (A-427, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.079 | 11/47 (NCI-H2030, A-427, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.079 | 6/47 (RKO, C-33 A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.090 | 4/45 (LOX-IMVI, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.099 | 7/46 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -6.9 | 3e-09 | 24/43 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.536×** | -6.5 | 2e-08 | 24/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.596×** | -5.4 | 1e-05 | 21/46 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.661×** | -4.3 | 0.002 | 18/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.502×** | -3.8 | 0.013 | 10/28 (CFPAC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.698×** | -3.8 | 0.013 | 17/46 (HEC-1-A, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.698×** | -3.8 | 0.013 | 14/47 (HEC-1-A, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.685×** | -3.7 | 0.013 | 15/44 (J82, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.013 | 16/47 (Hs 766T, LS 180, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.699×** | -3.6 | 0.017 | 15/37 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.720×** | -3.4 | 0.030 | 11/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -3.1 | 0.080 | 7/48 (AN3 CA, SNU-1, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | 0.575× | -3.0 | 0.10 | 11/45 (KATO III, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -9.9) |
| [[J82 (line)]] | alt | 9.46 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -9.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 4.89 | 0 | 2 (1 ⚠) | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0576× (z -10.0) |
| [[A498 (line)]] | wt | 2.94 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0550× (z -10.1) |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0564× (z -10.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[H4 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0681× (z -11.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 9.95 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -9.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 6.23 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0567× (z -12.0) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H1792 (line)]] | alt | 8.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0533× (z -13.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0662× (z -13.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200A]] | +0.85 | +0.88 / +0.62 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.81 | +0.82 / +0.66 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.80 | +0.85 / +0.53 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.79 | +0.81 / +0.57 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.79 | +0.80 / +0.51 | both halves | 1e-05 | same gene group |
| [[RAB30-DT]] | +0.78 | +0.85 / +0.44 | both halves | 3e-05 |  |
| [[KRCC1]] | +0.77 | +0.84 / +0.54 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.77 | +0.84 / +0.47 | both halves | 2e-05 |  |
| [[METTL6]] | +0.77 | +0.82 / +0.40 | both halves | 5e-05 |  |
| [[THBS4]] | +0.77 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ZNF594]] | +0.76 | +0.84 / +0.56 | both halves | 1e-05 |  |
| [[ZNF189]] | +0.76 | +0.73 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.69 | -0.72 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRIP1]] | B | NRIP1 activity lowers ZNF407-AS1's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.64× higher at baseline in the lines without NRIP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises ZNF407-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ZNF407-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CARD6]] | B | CARD6 activity lowers ZNF407-AS1's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.35× higher at baseline in the lines without CARD6 | 0.099 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZEB1-AS1]] | C | ZNF407-AS1's natural level weakens ZEB1-AS1's drug response | ZNF407-AS1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.10; direction not clear | 0.053 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.770). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.1, 14.2); signed map (12.5, -21.6). **Vector** length 73.7, 13.3% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.8 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.9 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.7 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.4 | -3.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ZNF407 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18q22.3 — chr18:74,590,317-74,598,885 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC00909 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44331) · Entrez [400657](https://www.ncbi.nlm.nih.gov/gene/400657) · Ensembl [ENSG00000264247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000264247)

## Data

Gene col 15435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15435); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15435]; `tensor/DDL_lfc|DDL_z.npy` [15435]; `embed/gene_vectors.npy` [15435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15435 or target_col == 15435). Every well: [[ZNF407-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF407-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
