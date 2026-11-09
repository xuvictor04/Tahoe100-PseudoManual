---
symbol: "ID1"
type: "gene"
col: 4700
ensembl_id: "ENSG00000125968"
name: "inhibitor of DNA binding 1"
location: "20q11.21"
module: 113
arm: "+"
pooled_cpm: 61.95
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# ID1

*inhibitor of DNA binding 1* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 2.13× (z +4.7, q 0.002, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.442× (z -7.1, q 6e-10, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1X]] (+0.76, fdr 7e-06), [[MT2A]] (+0.67, fdr 1e-05), [[ZMYND8]] (+0.66, fdr 7e-06); moves opposite to [[ZMPSTE24]] (-0.50, fdr 8e-04, ⚠ not reproduced), [[RCN1]] (-0.49, fdr 2e-04), [[FSTL1]] (-0.49, fdr 2e-04), [[MOB1A]] (-0.49, fdr 3e-04).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PGM5P2-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.13×** | +4.7 | 0.002 | 32/47 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.014 | 35/47 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.91×** | +4.0 | 0.014 | 31/47 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.75×** | +3.5 | 0.070 | 26/47 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.73×** | +3.4 | 0.079 | 23/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +3.3 | 0.083 | 30/47 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.70×** | +3.3 | 0.083 | 27/47 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.68×** | +3.2 | 0.090 | 28/47 (SW1417, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.100 | 24/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.442×** | -7.1 | 6e-10 | 35/47 (Hs 766T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.328×** | -6.9 | 2e-09 | 41/47 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.368×** | -6.2 | 1e-07 | 36/47 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.390×** | -5.5 | 5e-06 | 40/47 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.563×** | -5.0 | 6e-05 | 34/47 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.459×** | -4.8 | 1e-04 | 29/47 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.462×** | -4.8 | 1e-04 | 34/47 (BT-474, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.449×** | -4.8 | 1e-04 | 28/39 (NCI-H661, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.443×** | -4.7 | 1e-04 | 31/47 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.503×** | -4.1 | 0.003 | 32/47 (HT-29, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.520×** | -4.0 | 0.003 | 32/47 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.538×** | -3.8 | 0.006 | 32/47 (SW48, A498, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.664×** | -3.6 | 0.016 | 33/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.564×** | -3.5 | 0.016 | 29/46 (HEC-1-A, SHP-77, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.565×** | -3.5 | 0.016 | 31/47 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.573×** | -3.4 | 0.021 | 27/47 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.314×** | -3.4 | 0.026 | 33/47 (BT-474, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[crizotinib (drug)]] 5 µM |  | **0.571×** | -3.3 | 0.028 | 33/47 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.331×** | -3.2 | 0.036 | 26/48 (SNU-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 193 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0815× (z -17.2) |
| [[Hs 766T (line)]] | wt | 191 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0908× (z -19.0) |
| [[A-172 (line)]] | wt | 117 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -15.8) |
| [[BT-474 (line)]] | alt | 69.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -11.2) |
| [[KATO III (line)]] | alt | 110 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0919× (z -12.3) |
| [[A549 (line)]] | wt | 94.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 83.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.189× (z -11.9) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -11.4) |
| [[A-427 (line)]] | wt | 43.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.232× (z -11.8) |
| [[AN3 CA (line)]] | alt | 63.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -8.7) |
| [[HOP62 (line)]] | alt | 89.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -10.3) |
| [[LoVo (line)]] | wt | 41.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -8.8) |
| [[LS 180 (line)]] | wt | 62.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 59.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -12.9) |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0658× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 48.0 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.120× (z -9.0) |
| [[SHP-77 (line)]] | alt | 48.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -9.2) |
| [[SNU-1 (line)]] | wt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -8.9) |
| [[SNU-423 (line)]] | alt | 74.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -9.1) |
| [[SW48 (line)]] | wt | 62.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -10.2) |
| [[A498 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1X]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[MT2A]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZMYND8]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MT1F]] | +0.66 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[SAA1]] | +0.65 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[MT1E]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[MIDN]] | +0.64 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[IRX3]] | +0.60 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[MT1A]] | +0.60 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[TBC1D8]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DUSP1]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN; STRING 434 |
| [[TIPARP]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMPSTE24]] | -0.50 | -0.20 / -0.47 | ⚠ not reproduced | 8e-04 |  |
| [[RCN1]] | -0.49 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[FSTL1]] | -0.49 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[UBE2V1]] | -0.49 | -0.14 / -0.52 | ⚠ one half (not replicated) | 0.002 |  |
| [[MOB1A]] | -0.49 | -0.26 / -0.48 | both halves | 3e-04 |  |
| [[STMP1]] | -0.49 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[DPY19L4]] | -0.49 | -0.12 / -0.59 | ⚠ one half (not replicated) | 0.002 |  |
| [[DHFR]] | -0.49 | -0.08 / -0.53 | ⚠ one half (not replicated) | 0.003 |  |
| [[AP2B1]] | -0.48 | -0.25 / -0.53 | both halves | 4e-04 | pathway: Signaling by NTRK1 (TRKA) |
| [[PSMD6-AS1]] | -0.48 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[PSME3IP1]] | -0.48 | -0.19 / -0.46 | ⚠ not reproduced | 8e-04 |  |
| [[PGM5P2-1]] | -0.48 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGM5P2-1]] | B | PGM5P2-1 activity lowers ID1's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 1.70× higher at baseline in the lines without PGM5P2-1 | 0.0999 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.3, 13.4); signed map (14.3, 31.3). **Vector** length 130, 47.0% of its response variance represented; |z| ≥ 3 in 1,281 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.67 to 5); *metallothionein* (control, mean cos +0.67 to 5); *Response to metal ions* (reactome, mean cos +0.67 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.7 | +2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.0 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +3.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.5 | +4.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.3 | +3.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.1 | +3.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.4 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.4 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.7 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.3 | -3.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -5.1 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.0 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.1 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -1.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of DNA binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:31,605,283-31,606,515 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ857M17.1.2, bHLHb24 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; Inhibitor of DNA binding family |
| Hallmark sets | TGF_BETA_SIGNALING, UV_RESPONSE_DN |
| Reactome | 11 pathways, smallest: Oncogene Induced Senescence; NGF-stimulated transcription; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P41134](https://www.uniprot.org/uniprotkb/P41134) (DNA-binding protein inhibitor ID-1):

> Transcriptional regulator (lacking a basic DNA binding domain) which negatively regulates the basic helix-loop-helix (bHLH) transcription factors by forming heterodimers and inhibiting their DNA binding and transcriptional activity. Implicated in regulating a variety of cellular processes, including cellular growth, senescence, differentiation, apoptosis, angiogenesis, and neoplastic transformation. Inhibits skeletal muscle and cardiac myocyte differentiation. Regulates the circadian clock by …

**Summary**, from NCBI Gene [3397](https://www.ncbi.nlm.nih.gov/gene/3397):

> The protein encoded by this gene is a helix-loop-helix (HLH) protein that can form heterodimers with members of the basic HLH family of transcription factors. The encoded protein has no DNA binding activity and therefore can inhibit the DNA binding and transcriptional activation ability of basic HLH proteins with which it interacts. This protein may play a role in cell growth, senescence, and differentiation. Two transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:5360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5360) · Entrez [3397](https://www.ncbi.nlm.nih.gov/gene/3397) · UniProt [P41134](https://www.uniprot.org/uniprotkb/P41134) · Ensembl [ENSG00000125968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125968)

## Data

Gene col 4700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4700); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4700]; `tensor/DDL_lfc|DDL_z.npy` [4700]; `embed/gene_vectors.npy` [4700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4700 or target_col == 4700). Every well: [[ID1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ID1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
