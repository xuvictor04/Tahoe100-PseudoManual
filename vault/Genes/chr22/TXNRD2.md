---
symbol: "TXNRD2"
type: "gene"
col: 11541
ensembl_id: "ENSG00000184470"
name: "thioredoxin reductase 2"
location: "22q11.21"
module: 88
arm: "+"
pooled_cpm: 14.92
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# TXNRD2

*thioredoxin reductase 2* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.44× (z +6.6, q 2e-08, up in 21 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.36× (z +5.5, q 9e-06, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.257× (z -24.4, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H7B]] (+0.78, fdr 7e-06), [[DIS3L]] (+0.72, fdr 1e-05), [[CARD8]] (+0.72, fdr 7e-06); moves opposite to [[UBA6]] (-0.66, fdr 3e-05), [[CARHSP1]] (-0.63, fdr 1e-05), [[IGSF8]] (-0.63, fdr 6e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PMP22]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.6 | 2e-08 | 21/36 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.5 | 9e-06 | 24/45 (LS 180, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.6 | 8e-04 | 1/47 (AsPC-1) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +4.5 | 8e-04 | 17/31 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.5 | 8e-04 | 15/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.4 | 9e-04 | 15/26 (NCI-H1573, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.003 | 14/46 (C32, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.072 | 6/47 (RKO, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.072 | 8/47 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.11 | 11/39 (CFPAC-1, Panc 03.27, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.257×** | -24.4 | 0e+00 | 47/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.267×** | -23.8 | 0e+00 | 44/46 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.297×** | -21.9 | 0e+00 | 42/47 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.479×** | -13.3 | 5e-38 | 42/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -13.2 | 9e-38 | 35/45 (Hs 766T, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.521×** | -11.8 | 5e-30 | 35/43 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.711×** | -8.7 | 3e-16 | 34/47 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.454×** | -7.4 | 7e-12 | 23/47 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -7.4 | 8e-12 | 24/46 (HT-29, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.680×** | -7.0 | 2e-10 | 22/46 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.683×** | -6.9 | 3e-10 | 24/47 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.699×** | -6.5 | 5e-09 | 21/45 (SHP-77, SW48, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.748×** | -5.2 | 7e-06 | 19/45 (SW48, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.746×** | -5.1 | 1e-05 | 20/46 (SK-MEL-2, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -5.0 | 2e-05 | 18/46 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.780×** | -4.2 | 8e-04 | 11/44 (SW 1088, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.673×** | -3.7 | 0.005 | 13/43 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.692×** | -3.5 | 0.014 | 13/43 (HT-29, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 30.8 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.57× (z +13.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.179× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 15.0 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.254× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 0 | 6 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -13.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.213× (z -10.2) |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.120× (z -11.8) |
| [[SW480 (line)]] | alt | 15.4 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -14.1) |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -12.5) |
| [[KATO III (line)]] | alt | 16.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 26.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -12.0) |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -10.8) |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -11.7) |
| [[A-172 (line)]] | wt | 14.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +10.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.242× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.246× (z -11.2) |
| [[LoVo (line)]] | wt | 11.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 23.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0263× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 19.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.307× (z -10.2) |
| [[A-427 (line)]] | wt | 8.30 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0638× (z -13.7) |
| [[C-33 A (line)]] | alt | 20.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.129× (z -10.3) |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -10.0) |
| [[SHP-77 (line)]] | alt | 8.47 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0921× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 12.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.312× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 9.34 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -9.9) |
| [[C32 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -9.0) |
| [[H4 (line)]] | wt | 7.81 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0613× (z -9.0) |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 7.86 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0861× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -8.5) |
| [[LS 180 (line)]] | wt | 14.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.237× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.269× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -12.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[SW48 (line)]] | wt | 13.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.110× (z -9.4) |
| [[A549 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H7B]] | +0.78 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[DIS3L]] | +0.72 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[CARD8]] | +0.72 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[NFYC]] | +0.69 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SMARCB1]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[GABPB2]] | +0.68 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[INTS14]] | +0.68 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[FAIM]] | +0.67 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PYM1]] | +0.67 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[FKRP]] | +0.67 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[DLG5]] | +0.66 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA6]] | -0.66 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[CARHSP1]] | -0.63 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.63 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[DNAAF3]] | -0.63 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[GMCL1]] | -0.63 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[GNB2]] | -0.62 | -0.57 / -0.43 | both halves | 4e-05 |  |
| [[HDAC3]] | -0.62 | -0.52 / -0.53 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[MOSPD3]] | -0.62 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[PLA2G15]] | -0.61 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[CARD19]] | -0.61 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[SAP130]] | -0.60 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[HK1]] | -0.60 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMP22]] | B | PMP22 activity lowers TXNRD2's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.35× higher at baseline in the lines without PMP22 | 0.073 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-17.5, 5.6); signed map (10.3, -34.8). **Vector** length 78.7, 14.9% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.5 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.3 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +2.8 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -13.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -11.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -23.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -8.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -21.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -7.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin reductase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,875,517-19,941,820 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TR, TRXR2, TR3, SELZ, TXNR2 |
| Gene groups (HGNC) | Selenoproteins; Flavoproteins; Thioredoxin reductase family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 4 pathways, smallest: Detoxification of Reactive Oxygen Species; Cellular response to chemical stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NNW7](https://www.uniprot.org/uniprotkb/Q9NNW7) (Thioredoxin reductase 2, mitochondrial):

> Involved in the control of reactive oxygen species levels and the regulation of mitochondrial redox homeostasis. Maintains thioredoxin in a reduced state. May play a role in redox-regulated cell signaling.

**Summary**, from NCBI Gene [10587](https://www.ncbi.nlm.nih.gov/gene/10587):

> The protein encoded by this gene belongs to the pyridine nucleotide-disulfide oxidoreductase family, and is a member of the thioredoxin (Trx) system. Three thioredoxin reductase (TrxR) isozymes are found in mammals. TrxRs are selenocysteine-containing flavoenzymes, which reduce thioredoxins, as well as other substrates, and play a key role in redox homoeostasis. This gene encodes a mitochondrial form important for scavenging reactive oxygen species in mitochondria. It functions as a homodimer …

**Accessions** — [HGNC:18155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18155) · Entrez [10587](https://www.ncbi.nlm.nih.gov/gene/10587) · UniProt [Q9NNW7](https://www.uniprot.org/uniprotkb/Q9NNW7) · Ensembl [ENSG00000184470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184470)

## Data

Gene col 11541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11541); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11541]; `tensor/DDL_lfc|DDL_z.npy` [11541]; `embed/gene_vectors.npy` [11541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11541 or target_col == 11541). Every well: [[TXNRD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNRD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
