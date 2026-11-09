---
symbol: "TXK"
type: "gene"
col: 1097
ensembl_id: "ENSG00000074966"
name: "TXK tyrosine kinase"
location: "4p12"
module: 39
arm: "+"
pooled_cpm: 13.68
n_lines_expressing: 43
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# TXK

*TXK tyrosine kinase* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +11.2, q 2e-26, up in 30 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.343× (z -11.1, q 1e-25, down in 31 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.430× (z -8.7, q 7e-16, down in 29 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP50]] (+0.77, fdr 7e-06), [[GARIN1A]] (+0.76, fdr 7e-06), [[MPP4]] (+0.75, fdr 7e-06); moves opposite to [[COPG2]] (-0.60, fdr 5e-05), [[MPPE1]] (-0.60, fdr 3e-05), [[PXMP4]] (-0.58, fdr 5e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GARIN1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +11.2 | 2e-26 | 30/41 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.7 | 7e-16 | 32/38 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +7.5 | 1e-11 | 28/41 (HT-29, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +5.3 | 2e-05 | 19/40 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.1 | 4e-05 | 20/40 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +4.9 | 7e-05 | 19/40 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.40×** | +4.9 | 7e-05 | 22/41 (NCI-H2347, A-427, …) | rises with dose | low cells (technical?); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.56×** | +4.6 | 3e-04 | 21/41 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.003 | 18/41 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.016 | 13/41 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.045 | 16/41 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.047 | 6/41 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1097.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.343×** | -11.1 | 1e-25 | 31/39 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.430×** | -8.7 | 7e-16 | 29/41 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.253×** | -7.4 | 2e-11 | 30/41 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -7.4 | 2e-11 | 29/41 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.502×** | -7.1 | 1e-10 | 30/41 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.329×** | -6.0 | 2e-07 | 24/39 (HEC-1-A, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.601×** | -5.1 | 3e-05 | 18/35 (SNU-423, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.642×** | -4.4 | 7e-04 | 19/41 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.694×** | -3.8 | 0.010 | 16/35 (NCI-H2030, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.639×** | -3.5 | 0.021 | 16/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.785×** | -3.5 | 0.021 | 12/41 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.032 | 16/41 (C32, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.667×** | -3.2 | 0.060 | 14/41 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.068 | 15/41 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **0.747×** | -3.0 | 0.096 | 10/41 (NCI-H2030, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 58.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Verteporfin (drug)]] 5 µM 0.255× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 16.1 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.0334× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0981× (z -11.6) |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0389× (z -15.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 18.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +19.1) | — |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.126× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 9.70 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +14.2) | [[Verteporfin (drug)]] 5 µM 0.129× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.138× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0518× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -11.6) |
| [[A-427 (line)]] | wt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0941× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 9.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 7.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 5.35 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.05 µM 0.0579× (z -9.3) |
| [[HT-29 (line)]] | alt | 9.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.16× (z +12.2) | — |
| [[KATO III (line)]] | alt | 12.6 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0204× (z -9.8) |
| [[LS 180 (line)]] | wt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~54% of this change |
| [[SW480 (line)]] | alt | 9.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +12.0) | — |
| [[A-172 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP50]] | +0.77 | +0.82 / +0.67 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.76 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[MPP4]] | +0.75 | +0.78 / +0.67 | both halves | 7e-06 | same gene group |
| [[SLC22A1]] | +0.75 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[OIT3]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.71 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[PILRA]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.70 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[FAM151B]] | +0.70 | +0.77 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPG2]] | -0.60 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[MPPE1]] | -0.60 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PXMP4]] | -0.58 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TXK's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GARIN1A]] | B | TXK activity lowers GARIN1A's level | lines that do not express TXK (7) vs lines expressing it (43) | 1.02× higher at baseline in the lines without TXK | 0.089 | ⚠ within organs, on part of the lines; also absent: TEC; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.3, -13.1); signed map (18.0, 8.6). **Vector** length 91.4, 20.6% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.1 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.1 | -5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -4.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | TXK tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:48,066,393-48,134,250 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TKL, PSCTK5, BTKL, RLK; previously PTK4 |
| Gene groups (HGNC) | SH2 domain containing; Tec family tyrosine kinases; SH3 domain containing |
| Reactome | 3 pathways, smallest: FCERI mediated Ca+2 mobilization; Fc epsilon receptor (FCERI) signaling; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P42681](https://www.uniprot.org/uniprotkb/P42681) (Tyrosine-protein kinase TXK):

> Non-receptor tyrosine kinase that plays a redundant role with ITK in regulation of the adaptive immune response. Regulates the development, function and differentiation of conventional T-cells and nonconventional NKT-cells. When antigen presenting cells (APC) activate T-cell receptor (TCR), a series of phosphorylation leads to the recruitment of TXK to the cell membrane, where it is phosphorylated at Tyr-420. Phosphorylation leads to TXK full activation. Also contributes to signaling from many …

**Summary**, from NCBI Gene [7294](https://www.ncbi.nlm.nih.gov/gene/7294):

> Predicted to enable non-membrane spanning protein tyrosine kinase activity. Involved in positive regulation of type II interferon-mediated signaling pathway; protein autophosphorylation; and regulation of gene expression. Located in cytosol; nuclear lumen; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12434) · Entrez [7294](https://www.ncbi.nlm.nih.gov/gene/7294) · UniProt [P42681](https://www.uniprot.org/uniprotkb/P42681) · Ensembl [ENSG00000074966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074966)

## Data

Gene col 1097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1097); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1097]; `tensor/DDL_lfc|DDL_z.npy` [1097]; `embed/gene_vectors.npy` [1097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1097 or target_col == 1097). Every well: [[TXK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
