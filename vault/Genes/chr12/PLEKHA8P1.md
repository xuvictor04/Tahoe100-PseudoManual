---
symbol: "PLEKHA8P1"
type: "gene"
col: 5541
ensembl_id: "ENSG00000134297"
name: "pleckstrin homology domain containing A8 pseudogene 1"
location: "12q12"
module: 80
arm: "+"
pooled_cpm: 14.94
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 16
n_dd_up_clean: 17
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# PLEKHA8P1

*pleckstrin homology domain containing A8 pseudogene 1* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.26× (z +17.4, q 0e+00, up in 39 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.494× (z -10.7, q 8e-24, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BFSP1]] (+0.63, fdr 1e-05), [[SSPN]] (+0.61, fdr 1e-04), [[WAKMAR2]] (+0.58, fdr 1e-04); moves opposite to [[VPS13D]] (-0.57, fdr 3e-05), [[PSMD9]] (-0.55, fdr 8e-05), [[BRF1]] (-0.54, fdr 9e-04, ⚠ one half only (not replicated)), [[HERC2P2]] (-0.53, fdr 1e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +17.4 | 0e+00 | 39/43 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +9.8 | 3e-20 | 38/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +7.2 | 1e-10 | 26/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.5 | 9e-09 | 23/44 (HOP62, BT-474, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +5.3 | 1e-05 | 21/45 (NCI-H23, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.2 | 2e-05 | 18/47 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.0 | 4e-05 | 19/44 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.7 | 2e-04 | 15/45 (A-172, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 5e-04 | 16/46 (A498, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.002 | 14/45 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.003 | 18/46 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +3.9 | 0.005 | 13/47 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.008 | 9/43 (A-172, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.009 | 8/47 (HEC-1-A, NCI-H1792, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.012 | 11/46 (NCI-H23, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.494×** | -10.7 | 8e-24 | 30/46 (PANC-1, A-172, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -8.9 | 1e-16 | 30/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.593×** | -7.9 | 5e-13 | 25/45 (PANC-1, HEC-1-A, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -7.7 | 1e-12 | 27/45 (PANC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -7.4 | 2e-11 | 25/40 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.644×** | -6.6 | 3e-09 | 24/46 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.690×** | -5.3 | 1e-05 | 19/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.705×** | -5.3 | 1e-05 | 22/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.724×** | -4.9 | 6e-05 | 17/46 (HOP62, Panc 03.27, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.734×** | -4.7 | 2e-04 | 21/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.749×** | -4.4 | 7e-04 | 15/43 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.775×** | -3.8 | 0.006 | 14/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.810×** | -3.2 | 0.066 | 13/46 (AN3 CA, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.675×** | -3.1 | 0.078 | 12/47 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.817×** | -3.0 | 0.088 | 12/37 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.818×** | -3.0 | 0.088 | 15/47 (NCI-H661, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.8 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 26.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 29.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -12.2) |
| [[A-172 (line)]] | wt | 11.3 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +10.8) | [[Digitoxin (drug)]] 0.5 µM 0.186× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 34.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.301× (z -8.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.329× (z -8.5) |
| [[SW480 (line)]] | alt | 23.0 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -11.8) |
| [[HOP62 (line)]] | alt | 10.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +8.7) | — |
| [[LoVo (line)]] | wt | 9.39 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.205× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 14.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -12.1) ⚠ toxic |
| [[A498 (line)]] | wt | 7.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +11.1) | — |
| [[A549 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 6.85 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0622× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0852× (z -9.4) |
| [[Hs 766T (line)]] | wt | 16.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 7.20 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[SNU-423 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 8.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 10 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BFSP1]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[SSPN]] | +0.61 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[WAKMAR2]] | +0.58 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[TRHDE]] | +0.58 | +0.59 / +0.31 | both halves | 2e-04 |  |
| [[ANO6]] | +0.57 | +0.48 / +0.32 | both halves | 1e-04 | ⚠ same locus (41.3 kb: neighbours can correlate without regulation) |
| [[ZBED5]] | +0.57 | +0.60 / +0.36 | both halves | 9e-05 |  |
| [[BCL10-AS1]] | +0.56 | +0.57 / +0.29 | both halves | 2e-04 |  |
| [[ZNF462]] | +0.56 | +0.60 / +0.29 | both halves | 2e-04 |  |
| [[MSANTD3-TMEFF1]] | +0.55 | +0.57 / +0.26 | both halves | 4e-04 |  |
| [[THAP2]] | +0.55 | +0.60 / +0.21 | both halves | 7e-04 |  |
| [[PPP1R1C]] | +0.54 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[LINC01358]] | +0.54 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[LINC01135]] | +0.53 | +0.50 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS13D]] | -0.57 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[PSMD9]] | -0.55 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[BRF1]] | -0.54 | -0.58 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[HERC2P2]] | -0.53 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[CEP131]] | -0.53 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[DHTKD1]] | -0.52 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[TSC2]] | -0.51 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ERI3]] | -0.51 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[CAPN7]] | -0.50 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[SNTA1]] | -0.50 | -0.52 / -0.23 | both halves | 5e-04 |  |
| [[UNC13B]] | -0.49 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[CABLES2]] | -0.49 | -0.44 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[HERC2P9]] | -0.49 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[INPP4A]] | -0.49 | -0.43 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLEKHA8P1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | PLEKHA8P1's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | PLEKHA8P1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.472 over the table, 0.074 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.2, 15.7); signed map (28.0, 3.8). **Vector** length 78.3, 14.8% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +17.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +3.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -7.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing A8 pseudogene 1 |
| Locus type | pseudogene |
| Location | 12q12 — chr12:45,173,190-45,174,713 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | FLJ14156; previously PLEKHA9 |
| Matched by | ensembl_id |

UniProt [O95397](https://www.uniprot.org/uniprotkb/O95397) carries no function annotation.

**Summary**, from NCBI Gene [51054](https://www.ncbi.nlm.nih.gov/gene/51054):

> Predicted to enable ceramide 1-phosphate binding activity and ceramide 1-phosphate transfer activity. Predicted to be involved in ER to Golgi ceramide transport and intermembrane lipid transfer. Predicted to be located in cytoplasm. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30222) · Entrez [51054](https://www.ncbi.nlm.nih.gov/gene/51054) · UniProt [O95397](https://www.uniprot.org/uniprotkb/O95397) · Ensembl [ENSG00000134297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134297)

## Data

Gene col 5541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5541); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5541]; `tensor/DDL_lfc|DDL_z.npy` [5541]; `embed/gene_vectors.npy` [5541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5541 or target_col == 5541). Every well: [[PLEKHA8P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHA8P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
