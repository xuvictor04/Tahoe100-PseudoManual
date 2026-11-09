---
symbol: "NBPF14"
type: "gene"
col: 15666
ensembl_id: "ENSG00000270629"
name: "NBPF member 14"
location: "1q21.2"
module: 226
arm: "+"
pooled_cpm: 28.37
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/226"]
generated_by: "tahoemap"
---

# NBPF14

*NBPF member 14* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.10× (z +29.6, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.298× (z -22.5, q 0e+00, down in 33 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.810× (z -3.9, q 0.010, down in 16 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF10]] (+0.91, fdr 7e-06), [[NBPF19]] (+0.89, fdr 7e-06), [[NOTCH2NLA]] (+0.83, fdr 7e-06); moves opposite to [[RPE]] (-0.61, fdr 1e-05), [[GSR]] (-0.60, fdr 1e-05), [[DNAJB11]] (-0.59, fdr 1e-05).
> It is in [[Module 226]], a single-armed module (NOTCH2 Activation and Transmission of Signal to the Nucleus).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[G0S2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.10×** | +29.6 | 0e+00 | 45/45 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.54×** | +16.6 | 0e+00 | 44/46 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.52×** | +9.0 | 6e-17 | 34/47 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +8.8 | 2e-16 | 34/46 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +7.2 | 6e-11 | 29/44 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.1 | 1e-10 | 31/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.44×** | +6.8 | 1e-09 | 21/45 (NCI-H460, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +6.4 | 1e-08 | 25/45 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 1e-07 | 27/46 (RPMI-7951, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 3e-04 | 15/46 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.5 | 4e-04 | 14/43 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.4 | 6e-04 | 0/46 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.005 | 7/46 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.007 | 10/43 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.021 | 17/43 (SW 900, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.021 | 11/45 (SW 900, SNU-423, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.036 | 10/43 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15666.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.298×** | -22.5 | 0e+00 | 33/40 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.379×** | -17.3 | 0e+00 | 26/29 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.476×** | -12.8 | 4e-35 | 26/33 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.780×** | -4.6 | 5e-04 | 20/46 (HOP62, hTERT-HPNE, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.810×** | -3.9 | 0.010 | 16/46 (HCT15, SW 1271, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.867× | -3.8 | 0.014 | 13/46 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.817×** | -3.8 | 0.014 | 12/46 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.820×** | -3.6 | 0.025 | 12/45 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.832×** | -3.4 | 0.036 | 15/46 (NCI-H1792, HEC-1-A, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.843× | -3.2 | 0.074 | 16/45 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.721×** | -3.2 | 0.074 | 9/44 (HS-578T, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.847× | -3.1 | 0.092 | 13/45 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.888× | -3.0 | 0.10 | 9/46 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 46.3 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.0633× (z -20.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 26.8 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -15.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 31.3 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +25.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 66.0 | 1 | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 3.28× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -19.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.8 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.5 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +24.6) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -19.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 42.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -14.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 32.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 13.4 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.6 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 53.4 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -13.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 69.0 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -17.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 60.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -15.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0843× (z -19.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 25.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -14.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 42.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -14.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 25.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -13.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 62.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0473× (z -17.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 10.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +11.1) | [[XRK3F2 (drug)]] 0.5 µM 0.0605× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 29.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +13.4) | — |
| [[Panc 03.27 (line)]] | alt | 46.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 34.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +14.4) | — |
| [[A-427 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -8.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -12.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -11.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +12.9) | — |
| [[RKO (line)]] | wt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.3) | — |
| [[SNU-1 (line)]] | wt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +14.6) | — |
| [[SW1417 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.5) | — |
| [[SW48 (line)]] | wt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +10.6) | — |
| [[SW480 (line)]] | alt | 8.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF10]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | same gene group |
| [[NBPF19]] | +0.89 | +0.86 / +0.88 | both halves | 7e-06 | same gene group |
| [[NOTCH2NLA]] | +0.83 | +0.83 / +0.80 | both halves | 7e-06 |  |
| [[NBPF26]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 | same gene group |
| [[NOTCH2NLB]] | +0.61 | +0.59 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[METTL23]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[FAM110A]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[TNRC6C]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ACAP1]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NFKBIE]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MARCHF9]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD12]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[FOXA2]] | +0.57 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPE]] | -0.61 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[GSR]] | -0.60 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[DNAJB11]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ADPGK]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.58 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[UBQLN1]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[MFN2]] | -0.57 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[TRRAP]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[NAA50]] | -0.57 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[AP3M1]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[NAXD]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[CIPC]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[G0S2]] | B | G0S2 activity raises NBPF14's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without G0S2 | 0.017 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[HMGN2P46]] | B | HMGN2P46 activity raises NBPF14's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without HMGN2P46 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[ANKRD20A9P]] | B | ANKRD20A9P activity weakens NBPF14's drug response | lines that do not express ANKRD20A9P (38) vs lines expressing it (9) | the lines without ANKRD20A9P respond 1.40× as strongly (z diff -1.44); rises at some drug-doses, falls at others (29% from rises): Dinaciclib 5 µM: 0.28x vs 0.62x (z diff -6.2); Dinaciclib 0.5 µM: 0.30x vs 0.78x (z diff -5.7); Homoharringtonine 0.5 µM: 1.58x vs 1.28x (z diff -1.5) | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 226]] — NOTCH2 Activation and Transmission of Signal to the Nucleus; 9 genes; every member is in the + arm (projection on the module's main direction 0.887). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.4, -29.5); signed map (44.6, -15.4). **Vector** length 95.6, 21.9% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NOTCH2 Activation and Transmission of Signal to the Nucleus* (reactome, mean cos +0.61 to 4); *Signaling by NOTCH2* (reactome, mean cos +0.61 to 4); *Pre-NOTCH Transcription and Translation* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +29.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +16.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +6.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.5 | -22.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:148,531,385-148,679,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DJ328E19.C1.1 |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [Q5TI25](https://www.uniprot.org/uniprotkb/Q5TI25) carries no function annotation.

**Summary**, from NCBI Gene [25832](https://www.ncbi.nlm.nih.gov/gene/25832):

> This gene is a member of the neuroblastoma breakpoint family (NBPF) which consists of dozens of recently duplicated genes primarily located in segmental duplications on human chromosome 1. This gene family has experienced its greatest expansion within the human lineage and has expanded, to a lesser extent, among primates in general. Members of this gene family are characterized by tandemly repeated copies of DUF1220 protein domains. Gene copy number variations in the human chromosomal region …

**Accessions** — [HGNC:25232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25232) · Entrez [25832](https://www.ncbi.nlm.nih.gov/gene/25832) · UniProt [Q5TI25](https://www.uniprot.org/uniprotkb/Q5TI25) · Ensembl [ENSG00000270629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270629)

## Data

Gene col 15666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15666); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15666]; `tensor/DDL_lfc|DDL_z.npy` [15666]; `embed/gene_vectors.npy` [15666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15666 or target_col == 15666). Every well: [[NBPF14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
