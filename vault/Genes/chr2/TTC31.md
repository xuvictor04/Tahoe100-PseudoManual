---
symbol: "TTC31"
type: "gene"
col: 3650
ensembl_id: "ENSG00000115282"
name: "tetratricopeptide repeat domain 31"
location: "2p13.1"
module: 127
arm: "+"
pooled_cpm: 11.28
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# TTC31

*tetratricopeptide repeat domain 31* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.62× (z +3.9, q 0.052, up in 3 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.427× (z -13.2, q 8e-37, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMAP1]] (+0.68, fdr 7e-06), [[PGAP3]] (+0.58, fdr 3e-05), [[C2CD5]] (+0.56, fdr 3e-05); moves opposite to [[GAN]] (-0.56, fdr 2e-05), [[PACS1]] (-0.48, fdr 1e-04), [[ATP6V0B]] (-0.47, fdr 1e-04).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF548]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.62×** | +3.9 | 0.052 | 3/46 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.3 | 0.26 | 3/48 (HOP62, NCI-H23, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.46 | 11/44 (hTERT-HPNE, HCT15, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.427×** | -13.2 | 8e-37 | 38/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.582×** | -8.4 | 2e-14 | 29/44 (SNU-423, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.685×** | -8.3 | 2e-14 | 28/47 (RPMI-7951, SNU-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.589×** | -8.2 | 4e-14 | 29/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.600×** | -7.9 | 3e-13 | 27/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.617×** | -7.5 | 7e-12 | 25/45 (J82, PANC-1, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.631×** | -7.1 | 1e-10 | 25/47 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.643×** | -6.8 | 6e-10 | 30/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -6.4 | 1e-08 | 24/47 (C-33 A, HEC-1-A, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.671×** | -6.2 | 4e-08 | 17/47 (NCI-H2030, PANC-1, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.714×** | -5.2 | 1e-05 | 15/47 (NCI-H2030, NCI-H23, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.716×** | -5.2 | 1e-05 | 18/47 (COLO 205, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.742×** | -4.6 | 2e-04 | 14/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.745×** | -4.3 | 7e-04 | 14/45 (MIA PaCa-2, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.751×** | -4.3 | 8e-04 | 16/44 (NCI-H23, SW48, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.758×** | -4.1 | 0.001 | 13/47 (NCI-H23, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.772×** | -4.0 | 0.002 | 14/47 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.774×** | -4.0 | 0.002 | 16/46 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.853× | -3.5 | 0.014 | 14/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.050 | 6/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.826×** | -3.0 | 0.070 | 14/44 (SW48, SK-MEL-2, …) | rises with dose |  |
| [[BI-78D3 (drug)]] 0.5 µM |  | **0.766×** | -2.9 | 0.070 | 4/48 (A-427, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 8.70 | 0 | 2 | — | [[Saquinavir (drug)]] 0.05 µM 0.0884× (z -8.7) |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -10.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 10.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.208× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 10.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0737× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0692× (z -14.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 8.59 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0917× (z -8.8) |
| [[Hs 766T (line)]] | wt | 6.29 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.109× (z -8.6) |
| [[J82 (line)]] | alt | 5.71 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0838× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -10.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.287× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.338× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0625× (z -14.0) |
| [[SNU-423 (line)]] | alt | 7.33 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0489× (z -13.0) |
| [[A-427 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMAP1]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[PGAP3]] | +0.58 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[C2CD5]] | +0.56 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[TMEM237]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PCIF1]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.55 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[HAUS5]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[HIRIP3]] | +0.54 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[POMK]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[BAP1]] | +0.54 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[PIGO]] | +0.53 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[STK11IP]] | +0.53 | +0.42 / +0.61 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAN]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[PACS1]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[ATP6V0B]] | -0.47 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[AHCYL1]] | -0.47 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PHKG1]] | -0.47 | -0.37 / -0.57 | both halves | 7e-05 |  |
| [[LRP2BP-AS1]] | -0.46 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[WNT2B]] | -0.46 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[TMEM38A]] | -0.45 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[LRRC23]] | -0.45 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[PPARA]] | -0.45 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[RABGEF1]] | -0.45 | -0.24 / -0.55 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF548]] | B | ZNF548 activity lowers TTC31's level | lines that do not express ZNF548 (6) vs lines expressing it (44) | 1.18× higher at baseline in the lines without ZNF548 | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF547, TRAPPC2B, ZNF264 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.2, 1.5); signed map (-10.7, -30.3). **Vector** length 56.3, 7.60% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -1.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.8 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | +3.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +1.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -2.2 | -7.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -6.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,483,073-74,494,559 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12788 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q49AM3](https://www.uniprot.org/uniprotkb/Q49AM3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25759) · Entrez [64427](https://www.ncbi.nlm.nih.gov/gene/64427) · UniProt [Q49AM3](https://www.uniprot.org/uniprotkb/Q49AM3) · Ensembl [ENSG00000115282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115282)

## Data

Gene col 3650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3650); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3650]; `tensor/DDL_lfc|DDL_z.npy` [3650]; `embed/gene_vectors.npy` [3650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3650 or target_col == 3650). Every well: [[TTC31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
