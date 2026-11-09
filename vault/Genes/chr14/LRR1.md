---
symbol: "LRR1"
type: "gene"
col: 9132
ensembl_id: "ENSG00000165501"
name: "leucine rich repeat protein 1"
location: "14q21.3"
module: 71
arm: "+"
pooled_cpm: 9.56
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# LRR1

*leucine rich repeat protein 1* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +16.8, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.693× (z -6.7, q 1e-08, down in 27 of 46 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Temsirolimus (drug)]] 0.5 µM: 0.722× (z -4.2, q 0.004, down in 12 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFWD3]] (+0.77, fdr 7e-06), [[POLA2]] (+0.76, fdr 7e-06), [[LIN9]] (+0.75, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +16.8 | 0e+00 | 39/44 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +9.5 | 4e-19 | 32/37 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **1.75×** | +7.2 | 2e-10 | 20/35 (A549, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.69×** | +6.5 | 1e-08 | 11/18 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.62×** | +5.9 | 3e-07 | 24/46 (LoVo, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.62×** | +5.9 | 3e-07 | 22/44 (SW480, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.59×** | +5.7 | 7e-07 | 21/44 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.49×** | +5.1 | 2e-05 | 14/39 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.32×** | +5.1 | 2e-05 | 15/48 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.43×** | +4.6 | 2e-04 | 16/46 (LoVo, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.40×** | +4.0 | 0.004 | 13/27 (CFPAC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.004 | 11/44 (COLO 205, SW48, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.34×** | +3.7 | 0.009 | 16/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.014 | 10/48 (SW480, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.29×** | +3.3 | 0.040 | 12/45 (COLO 205, HEC-1-A, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.070 | 6/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.074 | 6/47 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.693×** | -6.7 | 1e-08 | 27/46 (NCI-H1573, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.647×** | -5.6 | 5e-06 | 19/44 (A498, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.585×** | -4.9 | 2e-04 | 13/47 (PANC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.722×** | -4.2 | 0.004 | 12/44 (A549, H4, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.717×** | -4.0 | 0.006 | 12/48 (SNU-1, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.749×** | -3.7 | 0.017 | 12/48 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.829×** | -3.4 | 0.044 | 7/47 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.756×** | -3.4 | 0.044 | 11/44 (Hs 766T, SW48, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.783×** | -3.2 | 0.098 | 17/47 (J82, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.786×** | -3.1 | 0.098 | 6/47 (C32, SW 900, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.779×** | -3.1 | 0.098 | 12/43 (NCI-H460, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -20.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 7.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +10.0) | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.100× (z -8.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 8.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 7.44 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.256× (z -9.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[PANC-1 (line)]] | alt | 8.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[SW480 (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.5) | — |
| [[A-172 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFWD3]] | +0.77 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[POLA2]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[LIN9]] | +0.75 | +0.63 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ORC6]] | +0.75 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[GEN1]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[DBF4B]] | +0.72 | +0.62 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CENPO]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[C9orf40]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[VRK1]] | +0.71 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[DDIAS]] | +0.70 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[ZNF367]] | +0.70 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[GINS1]] | +0.70 | +0.75 / +0.74 | both halves | 7e-06 | STRING 869 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises LRR1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without E2F8 | 0.008 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers LRR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.8, -48.7); signed map (-42.1, -44.6). **Vector** length 81.0, 16.5% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +16.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.7 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.0 | +3.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.3 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[vincristine (drug)]] 0.05 µM |  | +1.2 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.2 | +0.8 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.2 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.6 | -6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -4.1 | -5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | -2.8 | -3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.0 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:49,598,761-49,614,672 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 4-1BBLRR, MGC20689, LRR-1; previously PPIL5 |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96L50](https://www.uniprot.org/uniprotkb/Q96L50) (Leucine-rich repeat protein 1):

> Substrate recognition subunit of an ECS (Elongin BC-CUL2/5-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. ECS(LRR1) ubiquitinates MCM7 and promotes CMG replisome disassembly by VCP and chromatin extraction during S-phase (By similarity). May negatively regulate the 4-1BB-mediated signaling cascades which result in the activation of NK-kappaB and JNK1.

**Summary**, from NCBI Gene [122769](https://www.ncbi.nlm.nih.gov/gene/122769):

> The protein encoded by this gene contains a leucine-rich repeat (LRR). It specifically interacts with TNFRSF9/4-1BB, a member of the tumor necrosis factor receptor (TNFR) superfamily. Overexpression of this gene suppresses the activation of NF-kappa B induced by TNFRSF9 or TNF receptor-associated factor 2 (TRAF2), which suggests that this protein is a negative regulator of TNFRSF9-mediated signaling cascades. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Feb …

**Accessions** — [HGNC:19742](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19742) · Entrez [122769](https://www.ncbi.nlm.nih.gov/gene/122769) · UniProt [Q96L50](https://www.uniprot.org/uniprotkb/Q96L50) · Ensembl [ENSG00000165501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165501)

## Data

Gene col 9132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9132); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9132]; `tensor/DDL_lfc|DDL_z.npy` [9132]; `embed/gene_vectors.npy` [9132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9132 or target_col == 9132). Every well: [[LRR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
