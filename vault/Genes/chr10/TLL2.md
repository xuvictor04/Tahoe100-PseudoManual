---
symbol: "TLL2"
type: "gene"
col: 1750
ensembl_id: "ENSG00000095587"
name: "tolloid like 2"
location: "10q24.1"
module: 47
arm: "+"
pooled_cpm: 6.79
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# TLL2

*tolloid like 2* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.22× (z +28.2, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.579× (z -5.5, q 2e-05, down in 18 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[LB-100 (drug)]] 0.05 µM: 0.660× (z -3.8, q 0.031, down in 1 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM72]] (+0.77, fdr 7e-06), [[SELPLG]] (+0.76, fdr 7e-06), [[HPX]] (+0.76, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.22×** | +28.2 | 0e+00 | 39/41 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **9.55×** | +22.8 | 0e+00 | 45/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.62×** | +21.8 | 0e+00 | 35/39 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.58×** | +20.4 | 0e+00 | 44/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.83×** | +19.4 | 0e+00 | 42/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.72×** | +18.7 | 0e+00 | 40/45 (SW480, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.73×** | +15.7 | 0e+00 | 41/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.81×** | +13.5 | 1e-39 | 27/40 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.33×** | +11.7 | 1e-29 | 31/39 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.32×** | +11.6 | 2e-29 | 31/40 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.85×** | +10.5 | 3e-24 | 27/45 (SW480, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.78×** | +10.3 | 3e-23 | 30/44 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.89×** | +9.0 | 8e-18 | 23/47 (PANC-1, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +8.8 | 5e-17 | 8/17 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.38×** | +8.7 | 8e-17 | 15/30 (AsPC-1, HOP62, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.05×** | +5.9 | 1e-07 | 18/43 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +5.7 | 3e-07 | 20/44 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -5.5 | 2e-05 | 18/42 (C-33 A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[LB-100 (drug)]] 0.05 µM |  | **0.660×** | -3.8 | 0.031 | 1/45 (SW 900) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -3.8 | 0.031 | 17/45 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.520×** | -3.5 | 0.077 | 13/37 (SW 900, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.05 µM |  | **0.693×** | -3.4 | 0.084 | 6/44 (COLO 205, Hs 766T, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.808× | -3.1 | 0.21 | 5/46 (SHP-77, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.91 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +13.8) | — |
| [[SW480 (line)]] | alt | 4.53 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +15.3) | — |
| [[PANC-1 (line)]] | alt | 4.49 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 25.9× (z +15.1) | — |
| [[LoVo (line)]] | wt | 13.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +18.8) | — |
| [[SW1417 (line)]] | alt | 9.98 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 4.64× (z +10.3) | — |
| [[A498 (line)]] | wt | 11.4 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +10.4) | — |
| [[A-172 (line)]] | wt | 5.02 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 4.05 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 3.24 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 5.72 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +13.8) | — |
| [[NCI-H2347 (line)]] | alt | 2.40 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.00× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 3.84 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.61× (z +8.8) | — |
| [[SW48 (line)]] | wt | 20.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +9.8) | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0795× (z -10.7) |
| [[A-427 (line)]] | wt | 18.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -11.9) |
| [[A549 (line)]] | wt | 2.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.6× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 4.66 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.2× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0835× (z -11.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 5.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 6.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 2.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.3× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 3.44 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 22.2× (z +8.5) | — |
| [[KATO III (line)]] | alt | 4.70 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0884× (z -8.5) |
| [[LS 180 (line)]] | wt | 2.55 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.2× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 38.3× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 7.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +10.3) | — |
| [[RKO (line)]] | wt | 5.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.60× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 2.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM72]] | +0.77 | +0.82 / +0.64 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[HPX]] | +0.76 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.75 | +0.80 / +0.67 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.75 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.74 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.74 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.73 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[XG]] | +0.73 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.72 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[SH2D4B]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TLL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MLIP]] | B | MLIP activity raises TLL2's level | lines that do not express MLIP (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without MLIP | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises TLL2's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.89× lower at baseline in the lines without ASGR1 | 0.069 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[HAP1]] | B | HAP1 activity strengthens TLL2's drug response | lines that do not express HAP1 (12) vs lines expressing it (34) | the lines without HAP1 respond 0.86× as strongly (z diff +1.06); strongest at Homoharringtonine 5 µM: 3.26x vs 4.51x (z diff +2.4) | 0.096 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.5, -15.6); signed map (17.1, 12.0). **Vector** length 65.8, 11.4% of its response variance represented; |z| ≥ 3 in 1,491 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +18.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.1 | +8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +28.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +10.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +9.0 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.8 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | tolloid like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:96,364,608-96,513,926 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Astacins |
| Reactome | 7 pathways, smallest: Anchoring fibril formation; Crosslinking of collagen fibrils; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6L7](https://www.uniprot.org/uniprotkb/Q9Y6L7) (Tolloid-like protein 2):

> Protease which specifically processes pro-lysyl oxidase. Required for the embryonic development. Predominant protease, which in the development, influences dorsal-ventral patterning and skeletogenesis.

**Summary**, from NCBI Gene [7093](https://www.ncbi.nlm.nih.gov/gene/7093):

> This gene encodes an astacin-like zinc-dependent metalloprotease and is a subfamily member of the metzincin family. Unlike other family members, a similar protein in mice does not cleave procollagen C-propeptides or chordin. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11844) · Entrez [7093](https://www.ncbi.nlm.nih.gov/gene/7093) · UniProt [Q9Y6L7](https://www.uniprot.org/uniprotkb/Q9Y6L7) · Ensembl [ENSG00000095587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095587)

## Data

Gene col 1750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1750); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1750]; `tensor/DDL_lfc|DDL_z.npy` [1750]; `embed/gene_vectors.npy` [1750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1750 or target_col == 1750). Every well: [[TLL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
