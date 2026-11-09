---
symbol: "TRPM2"
type: "gene"
col: 6602
ensembl_id: "ENSG00000142185"
name: "transient receptor potential cation channel subfamily M member 2"
location: "21q22.3"
module: 150
arm: "+"
pooled_cpm: 2.82
n_lines_expressing: 39
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# TRPM2

*transient receptor potential cation channel subfamily M member 2* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.52× (z +17.6, q 0e+00, up in 16 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (HOP62 0.0513×, SHP-77 0.0811×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.0972×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.126×; ⚠ cell-cycle shift, explains ~18% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALOXE3]] (+0.64, fdr 1e-05), [[DGUOK-AS1]] (+0.64, fdr 1e-05), [[NANOS3]] (+0.63, fdr 1e-05); moves opposite to [[PPP1R12B]] (-0.52, fdr 2e-04), [[SPAST]] (-0.51, fdr 3e-05), [[GOLM2]] (-0.50, fdr 7e-05).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[FBN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.52×** | +17.6 | 0e+00 | 16/24 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +13.4 | 3e-38 | 14/27 (SNU-423, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +9.9 | 6e-21 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +8.2 | 4e-14 | 2/9 (SNU-423, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +7.6 | 3e-12 | 1/3 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +6.4 | 2e-08 | 13/30 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +5.7 | 1e-06 | 7/22 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +5.3 | 7e-06 | 9/27 (SW480, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.7 | 1e-04 | 2/12 (LS 180, NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.6 | 3e-04 | 4/13 (KATO III, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.004 | 7/33 (HOP62, HS-578T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +3.7 | 0.011 | 6/32 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.015 | 8/33 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.018 | 3/23 (RPMI-7951, NCI-H23, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.4 | 0.021 | 4/13 (NCI-H1573, SHP-77, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.024 | 4/17 (A-427, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.77×** | +3.0 | 0.087 | 1/13 (HOP62) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.090 | 3/33 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6602.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (HOP62 0.0513×, SHP-77 0.0811×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.0972×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.126×; ⚠ cell-cycle shift, explains ~18% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.690× | -3.4 | 0.39 | 2/33 (SW 1271, hTERT-HPNE) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 8.23 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 22.8× (z +13.6) | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0811× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0972× (z -10.8) |
| [[A-172 (line)]] | wt | 0.829 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.1× (z +10.5) | — |
| [[A-427 (line)]] | wt | 8.90 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -9.5) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HOP62 (line)]] | alt | 6.21 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0513× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 7.56 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 1.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 50.8× (z +13.3) | — |
| [[A498 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.817 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.727 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.752 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.746 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.708 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALOXE3]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[DGUOK-AS1]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.63 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[GRIA4]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[DLGAP2]] | +0.62 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[IL34]] | +0.62 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[THSD7B]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[LETM2]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[IPCEF1]] | +0.59 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[RELN]] | +0.59 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[GASAL1]] | +0.58 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[PLXNA4]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12B]] | -0.52 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[SPAST]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[GOLM2]] | -0.50 | -0.44 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBN2]] | B | TRPM2 activity raises FBN2's level | lines that do not express TRPM2 (11) vs lines expressing it (39) | 2.04× lower at baseline in the lines without TRPM2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[GOLM2]] | B | TRPM2 activity raises GOLM2's level | lines that do not express TRPM2 (11) vs lines expressing it (39) | 1.19× lower at baseline in the lines without TRPM2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[CCDC73]] | B | TRPM2 activity lowers CCDC73's level | lines that do not express TRPM2 (11) vs lines expressing it (39) | 1.32× higher at baseline in the lines without TRPM2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[SCARF1]] | B | TRPM2 activity lowers SCARF1's level | lines that do not express TRPM2 (11) vs lines expressing it (39) | 1.67× higher at baseline in the lines without TRPM2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.9, 22.5); signed map (28.0, 11.9). **Vector** length 38.4, 5.13% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +17.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -3.4 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.0 | -0.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily M member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,350,163-44,443,081 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KNP3, LTRPC2, NUDT9L1, NUDT9H, EREG1; previously TRPC7 |
| Gene groups (HGNC) | Nudix hydrolase family; Transient receptor potential cation channel subfamily M |
| Reactome | 6 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O94759](https://www.uniprot.org/uniprotkb/O94759) (Transient receptor potential cation channel subfamily M member 2):

> [Isoform 1]: Nonselective, voltage-independent cation channel that mediates Na(+) and Ca(2+) influx, leading to increased cytoplasmic Ca(2+) levels. Functions as a ligand-gated ion channel, gated by intracellular adenosine diphosphate ribose (ADP-ribose), Ca(2+), warm temperature, and oxidative stress. The precise physiological activators are under debate; the true, physiological activators may be ADP-ribose and ADP-ribose-2'-phosphate. Binding of ADP-ribose to the cytoplasmic Nudix domain …

**Summary**, from NCBI Gene [7226](https://www.ncbi.nlm.nih.gov/gene/7226):

> The protein encoded by this gene forms a tetrameric cation channel that is permeable to calcium, sodium, and potassium and is regulated by free intracellular ADP-ribose. The encoded protein is activated by oxidative stress and confers susceptibility to cell death. Alternative splicing results in multiple transcript variants encoding distinct protein isoforms. Additional transcript variants of this gene have been described, but their full-length nature is not known. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:12339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12339) · Entrez [7226](https://www.ncbi.nlm.nih.gov/gene/7226) · UniProt [O94759](https://www.uniprot.org/uniprotkb/O94759) · Ensembl [ENSG00000142185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142185)

## Data

Gene col 6602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6602); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6602]; `tensor/DDL_lfc|DDL_z.npy` [6602]; `embed/gene_vectors.npy` [6602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6602 or target_col == 6602). Every well: [[TRPM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
