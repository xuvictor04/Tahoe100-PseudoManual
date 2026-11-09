---
symbol: "ASIC2"
type: "gene"
col: 2987
ensembl_id: "ENSG00000108684"
name: "acid sensing ion channel subunit 2"
location: "17q11.2-q12"
module: 165
arm: "+"
pooled_cpm: 14.55
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# ASIC2

*acid sensing ion channel subunit 2* — 17q11.2-q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.23× (z +23.4, q 0e+00, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.761× (z -3.8, q 0.063, down in 13 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.176×, SHP-77 0.209×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.296×, SHP-77 0.354×); [[Digitoxin (drug)]] 5 µM in 2 lines (SHP-77 0.182×, PANC-1 0.208×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.187×, LoVo 0.151×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (LS 180 0.0677×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOS1]] (+0.72, fdr 7e-06), [[ABCA13]] (+0.68, fdr 7e-06), [[RBFOX3]] (+0.68, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PRKG1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2987.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +23.4 | 0e+00 | 29/37 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.93×** | +19.3 | 0e+00 | 20/26 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.06×** | +19.0 | 0e+00 | 8/13 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +17.9 | 0e+00 | 25/40 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +14.1 | 3e-43 | 16/20 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +8.1 | 7e-14 | 20/45 (A498, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +7.7 | 1e-12 | 18/42 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +7.6 | 2e-12 | 23/42 (SW480, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +6.9 | 5e-10 | 16/37 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.5 | 4e-09 | 13/37 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +5.6 | 1e-06 | 18/43 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.4 | 3e-06 | 14/35 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.009 | 12/42 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.010 | 7/43 (SK-MEL-2, CFPAC-1, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.6 | 0.014 | 4/13 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.020 | 6/41 (HOP62, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.044 | 2/41 (NCI-H460, SW48) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.060 | 5/38 (LoVo, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.063 | 11/45 (A498, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2987.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.176×, SHP-77 0.209×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.296×, SHP-77 0.354×); [[Digitoxin (drug)]] 5 µM in 2 lines (SHP-77 0.182×, PANC-1 0.208×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.187×, LoVo 0.151×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (LS 180 0.0677×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.761×** | -3.8 | 0.063 | 13/43 (NCI-H1792, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.768×** | -3.7 | 0.063 | 9/45 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -3.5 | 0.099 | 6/46 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 231 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.187× (z -10.4) |
| [[PANC-1 (line)]] | alt | 63.4 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.296× (z -11.1) |
| [[HOP62 (line)]] | alt | 6.92 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 18.3× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +9.2) | — |
| [[A498 (line)]] | wt | 15.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +15.1) | — |
| [[HS-578T (line)]] | alt | 16.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.82× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 3.37× (z +8.5) | — |
| [[LoVo (line)]] | wt | 18.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0353× (z -16.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.151× (z -9.5) |
| [[BT-474 (line)]] | alt | 6.13 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +8.7) | [[Erlotinib (drug)]] 5 µM 0.0752× (z -8.6) |
| [[C32 (line)]] | wt | 5.28 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.26× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 4.95 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.74× (z +12.8) | — |
| [[KATO III (line)]] | alt | 3.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +10.7) | — |
| [[SW480 (line)]] | alt | 4.34 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.01× (z +12.8) | — |
| [[A549 (line)]] | wt | 21.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 4.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0677× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.170× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 3.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.129× (z -8.8) |
| [[A-172 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOS1]] | +0.72 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[ABCA13]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[RBFOX3]] | +0.68 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.67 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[MTUS2]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[RYR3]] | +0.64 | +0.45 / +0.66 | both halves | 3e-05 | pathway: Ion channel transport |
| [[CCDC26]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CNTN5]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[BMAL2-AS1]] | +0.63 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[CDH23]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ATP8A2]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 | pathway: Ion channel transport |
| [[CNTNAP5]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKG1-AS1]] | B | PRKG1-AS1 activity lowers ASIC2's level | lines that do not express PRKG1-AS1 (15) vs lines expressing it (35) | 1.07× higher at baseline in the lines without PRKG1-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: HERC5, RAB31, GALC |
| [[NCF2]] | B | NCF2 activity strengthens ASIC2's drug response | lines that do not express NCF2 (9) vs lines expressing it (37) | the lines without NCF2 respond 0.30× as strongly (z diff +1.91); strongest at Dinaciclib 0.5 µM: 0.80x vs 3.82x (z diff +6.7) | 0.098 | ⚠ within organs, on part of the lines; also absent: MAML2; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.2, 31.0); signed map (30.7, 16.9). **Vector** length 74.5, 12.6% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.4 | +19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.4 | +19.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.1 | +14.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +23.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +17.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +1.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.6 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | acid sensing ion channel subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2-q12 — chr17:33,013,087-34,174,964 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASIC2a, BNC1, BNaC1, hBNaC1, MDEG; previously ACCN, ACCN1 |
| Gene groups (HGNC) | Acid sensing ion channel subunits |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16515](https://www.uniprot.org/uniprotkb/Q16515) (Acid-sensing ion channel 2):

> Forms pH-gated trimeric sodium channels that act as postsynaptic excitatory sensors in the nervous system. Upon extracellular acidification, these channels generate rapid, transient inward currents that fully desensitize. Highly selective for sodium, they are permeable to other cations. By forming heterotrimeric channels with ASIC1, could contribute to synaptic plasticity, learning, and memory. Additionally, as acid sensors at nerve terminals, plays a role in mechanosensation and …

**Summary**, from NCBI Gene [40](https://www.ncbi.nlm.nih.gov/gene/40):

> This gene encodes a member of the degenerin/epithelial sodium channel (DEG/ENaC) superfamily. The members of this family are amiloride-sensitive sodium channels that contain intracellular N and C termini, 2 hydrophobic transmembrane regions, and a large extracellular loop, which has many cysteine residues with conserved spacing. The member encoded by this gene may play a role in neurotransmission. In addition, a heteromeric association between this member and acid-sensing (proton-gated) ion …

**Accessions** — [HGNC:99](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:99) · Entrez [40](https://www.ncbi.nlm.nih.gov/gene/40) · UniProt [Q16515](https://www.uniprot.org/uniprotkb/Q16515) · Ensembl [ENSG00000108684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108684)

## Data

Gene col 2987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2987); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2987]; `tensor/DDL_lfc|DDL_z.npy` [2987]; `embed/gene_vectors.npy` [2987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2987 or target_col == 2987). Every well: [[ASIC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASIC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
