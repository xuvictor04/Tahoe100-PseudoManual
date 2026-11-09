---
symbol: "ORAI3"
type: "gene"
col: 10667
ensembl_id: "ENSG00000175938"
name: "ORAI calcium release-activated calcium modulator 3"
location: "16p11.2"
module: 118
arm: "+"
pooled_cpm: 8.07
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# ORAI3

*ORAI calcium release-activated calcium modulator 3* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Entrectinib (drug)]] 5 µM: 1.39× (z +4.0, q 0.042, up in 10 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.337× (z -12.9, q 3e-35, down in 31 of 42 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LZTS2]] (+0.52, fdr 9e-05), [[SPACDR]] (+0.50, fdr 3e-05), [[PI4KB]] (+0.50, fdr 2e-04); moves opposite to [[NRXN3]] (-0.49, fdr 1e-04), [[RSU1]] (-0.47, fdr 6e-04), [[SSX2IP]] (-0.47, fdr 4e-04).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MEST]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entrectinib (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.042 | 10/45 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.21× | +3.3 | 0.30 | 10/46 (SW 900, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10667.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.337×** | -12.9 | 3e-35 | 31/42 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.341×** | -12.7 | 1e-34 | 36/45 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.474×** | -12.5 | 1e-33 | 35/41 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.355×** | -12.3 | 2e-32 | 40/46 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.366×** | -11.9 | 1e-30 | 38/45 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.374×** | -11.6 | 2e-29 | 36/46 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.411×** | -10.5 | 5e-24 | 34/45 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.512×** | -7.6 | 2e-12 | 25/45 (COLO 205, MIA PaCa-2, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.296×** | -7.5 | 3e-12 | 27/42 (CFPAC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.532×** | -7.5 | 5e-12 | 29/41 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.540×** | -7.0 | 1e-10 | 22/35 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.560×** | -6.9 | 3e-10 | 27/44 (SW 900, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.568×** | -6.7 | 9e-10 | 24/44 (J82, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.360×** | -6.3 | 1e-08 | 26/39 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.611×** | -5.8 | 2e-07 | 24/46 (SW480, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.632×** | -5.4 | 2e-06 | 20/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.734×** | -5.2 | 8e-06 | 20/46 (A-172, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.509×** | -4.2 | 8e-04 | 13/43 (SK-MEL-2, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.709×** | -4.1 | 0.001 | 16/44 (SNU-423, MIA PaCa-2, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.737×** | -3.5 | 0.012 | 9/46 (CFPAC-1, MIA PaCa-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.9) |
| [[J82 (line)]] | alt | 8.44 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0733× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.148× (z -8.9) |
| [[SW480 (line)]] | alt | 8.76 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.6) |
| [[A-172 (line)]] | wt | 18.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 5.59 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0263× (z -19.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0988× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.153× (z -8.7) |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0516× (z -21.4) |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0610× (z -18.9) |
| [[HOP62 (line)]] | alt | 6.49 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 8.68 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0506× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 8.69 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 7.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -11.6) |
| [[BT-474 (line)]] | alt | 6.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0844× (z -12.2) |
| [[C-33 A (line)]] | alt | 8.13 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.5 µM 0.0777× (z -8.6) |
| [[COLO 205 (line)]] | alt | 8.91 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0603× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 5.16 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0660× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 7.54 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0666× (z -10.9) |
| [[LS 180 (line)]] | wt | 6.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0933× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 6.64 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -8.7) |
| [[RKO (line)]] | wt | 5.07 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0763× (z -8.6) |
| [[SW 900 (line)]] | alt | 6.73 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0932× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 6.31 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.119× (z -8.6) |
| [[A-427 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZTS2]] | +0.52 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[SPACDR]] | +0.50 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PI4KB]] | +0.50 | +0.29 / +0.49 | both halves | 2e-04 |  |
| [[NR1H3]] | +0.50 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[MTRFR]] | +0.49 | +0.23 / +0.57 | both halves | 5e-04 |  |
| [[ZNF446]] | +0.48 | +0.29 / +0.51 | both halves | 2e-04 |  |
| [[ZCCHC3]] | +0.48 | +0.21 / +0.55 | both halves | 6e-04 |  |
| [[NOXRED1]] | +0.48 | +0.29 / +0.51 | both halves | 2e-04 |  |
| [[EIF3J-DT]] | +0.47 | +0.24 / +0.47 | both halves | 5e-04 |  |
| [[KBTBD4]] | +0.47 | +0.25 / +0.54 | both halves | 4e-04 |  |
| [[NOL3]] | +0.46 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[IKZF4]] | +0.46 | +0.37 / +0.43 | both halves | 9e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRXN3]] | -0.49 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[RSU1]] | -0.47 | -0.21 / -0.43 | both halves | 6e-04 |  |
| [[SSX2IP]] | -0.47 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[DNAJC10]] | -0.47 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[PARK7]] ⚠ | -0.46 | -0.30 / -0.34 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[HLTF]] | -0.46 | -0.20 / -0.50 | ⚠ not reproduced | 8e-04 |  |
| [[ZDHHC21]] | -0.46 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[TLN2]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PODXL2]] | -0.45 | -0.22 / -0.40 | both halves | 6e-04 |  |
| [[EFR3A]] | -0.45 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[MEST]] | -0.43 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[HNRNPR]] | -0.43 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[APBB2]] | -0.43 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[LRRCC1]] | -0.43 | -0.25 / -0.46 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEST]] | B | MEST activity lowers ORAI3's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.50× higher at baseline in the lines without MEST | 0.050 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (29.5, -22.4); signed map (3.3, -3.4). **Vector** length 57.5, 8.83% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.6 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +1.5 | +0.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +4.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.1 | +1.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | -4.7 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -4.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ORAI calcium release-activated calcium modulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,949,068-30,956,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13024; previously TMEM142C |
| Gene groups (HGNC) | ORAI calcium release-activated calcium modulators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRQ5](https://www.uniprot.org/uniprotkb/Q9BRQ5) (Protein orai-3):

> Pore-forming subunit of two major inward rectifying Ca(2+) channels at the plasma membrane: Ca(2+) release-activated Ca(2+) (CRAC) channels and arachidonate-regulated Ca(2+)-selective (ARC) channels. Assembles with ORAI1 and ORAI2 to form hexameric CRAC channels that mediate Ca(2+) influx upon depletion of endoplasmic reticulum Ca(2+) store and channel activation by Ca(2+) sensor STIM1, a process known as store-operated Ca(2+) entry (SOCE). Various pore subunit combinations may account for …

**Summary**, from NCBI Gene [93129](https://www.ncbi.nlm.nih.gov/gene/93129):

> Enables store-operated calcium channel activity. Involved in store-operated calcium entry. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28185) · Entrez [93129](https://www.ncbi.nlm.nih.gov/gene/93129) · UniProt [Q9BRQ5](https://www.uniprot.org/uniprotkb/Q9BRQ5) · Ensembl [ENSG00000175938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175938)

## Data

Gene col 10667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10667); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10667]; `tensor/DDL_lfc|DDL_z.npy` [10667]; `embed/gene_vectors.npy` [10667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10667 or target_col == 10667). Every well: [[ORAI3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORAI3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
