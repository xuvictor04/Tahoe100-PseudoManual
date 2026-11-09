---
symbol: "HELLPAR"
type: "gene"
col: 15980
ensembl_id: "ENSG00000281344"
name: "HELLP associated long non-coding RNA"
location: "12q23.2"
module: 22
arm: "+"
pooled_cpm: 19.68
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# HELLPAR

*HELLP associated long non-coding RNA* — 12q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.53× (z +4.9, q 6e-04, up in 21 of 47 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.48× (z +4.5, q 0.001, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.693× (z -4.2, q 0.006, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAK6]] (+0.70, fdr 7e-06), [[ASPM]] (+0.68, fdr 7e-06), [[BIRC5]] (+0.68, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02456]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.53×** | +4.9 | 6e-04 | 21/47 (SHP-77, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.52×** | +4.6 | 0.001 | 18/47 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.54×** | +4.5 | 0.001 | 15/39 (SK-MEL-2, C32, …) | inconsistent across doses | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.48×** | +4.5 | 0.001 | 22/48 (SW480, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +4.3 | 0.002 | 21/48 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.011 | 15/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.020 | 14/47 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.025 | 18/47 (HepG2/C3A, RKO, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +3.5 | 0.031 | 16/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.77×** | +3.4 | 0.038 | 11/48 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.038 | 14/48 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.34×** | +3.2 | 0.068 | 13/47 (A-427, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.077 | 11/47 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.0 | 0.10 | 3/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM |  | **0.693×** | -4.2 | 0.006 | 22/47 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.773×** | -4.2 | 0.006 | 25/48 (C32, LS 180, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.780×** | -4.1 | 0.008 | 17/48 (LS 180, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.715×** | -3.7 | 0.021 | 18/46 (SNU-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.727×** | -3.7 | 0.021 | 15/47 (AN3 CA, HEC-1-A, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.728×** | -3.7 | 0.021 | 21/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM |  | **0.661×** | -3.4 | 0.051 | 17/48 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~21% here); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 15.0 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +11.0) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.86× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.219× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 17.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.74× (z +17.8) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[C32 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.261× (z -8.8) ⚠ cell-cycle shift, explains ~15% of this change |
| [[HEC-1-A (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0816× (z -9.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.113× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 31.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +11.4) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[HT-29 (line)]] | alt | 13.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.63× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +8.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +11.0) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[NCI-H23 (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 64.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0639× (z -12.2) ⚠ toxic |
| [[SW480 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -13.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAK6]] | +0.70 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ASPM]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[BIRC5]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[PRC1]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[FOXM1]] | +0.67 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[ZRANB3]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[KIF14]] | +0.67 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[HCCS-DT]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[ZNF876P]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LINC02456]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CENPN]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[KIF4A]] | +0.65 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[MKI67]] | +0.64 | +0.59 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02456]] | B | LINC02456 activity raises HELLPAR's level | lines that do not express LINC02456 (9) vs lines expressing it (41) | 2.15× lower at baseline in the lines without LINC02456 | 0.057 | ⚠ within organs, on part of the lines; also absent: GUCY1A2, OLFM2, ZNF610; maybe low, not absent |
| [[HERC2P10]] | B | HERC2P10 activity raises HELLPAR's level | lines that do not express HERC2P10 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without HERC2P10 | 0.079 | ⚠ within organs, on part of the lines; also absent: TENM3, SHANK1, TENM3-AS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers HELLPAR's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.7, -55.4); signed map (-49.4, -46.0). **Vector** length 107, 25.7% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.51 to 60); *DREAM G2/M down* (control, mean cos +0.56 to 28); *Resolution of Sister Chromatid Cohesion* (reactome, mean cos +0.50 to 33).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.2 | +4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.0 |
| fall | [[Selinexor (drug)]] 0.5 µM |  | -4.2 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.7 | -4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.2 | -3.7 |
|  | [[palbociclib (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | HELLP associated long non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q23.2 — chr12:102,197,585-102,402,596 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LINC-HELLP |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [101101692](https://www.ncbi.nlm.nih.gov/gene/101101692):

> Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:43984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43984) · Entrez [101101692](https://www.ncbi.nlm.nih.gov/gene/101101692) · Ensembl [ENSG00000281344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000281344)

## Data

Gene col 15980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15980); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15980]; `tensor/DDL_lfc|DDL_z.npy` [15980]; `embed/gene_vectors.npy` [15980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15980 or target_col == 15980). Every well: [[HELLPAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HELLPAR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
