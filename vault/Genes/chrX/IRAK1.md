---
symbol: "IRAK1"
type: "gene"
col: 11506
ensembl_id: "ENSG00000184216"
name: "interleukin 1 receptor associated kinase 1"
location: "Xq28"
module: 18
arm: "+"
pooled_cpm: 46.71
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# IRAK1

*interleukin 1 receptor associated kinase 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.33× (z +19.3, q 0e+00, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.77× (z +6.6, q 7e-09, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.608× (z -5.8, q 5e-06, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2G2]] (+0.67, fdr 7e-06), [[SPOPL-DT]] (+0.67, fdr 1e-05), [[METTL3]] (+0.64, fdr 1e-05); moves opposite to [[SECISBP2L]] (-0.59, fdr 1e-05), [[DBP]] (-0.59, fdr 3e-05), [[RNASE4]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PRDM5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TMTC4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.33×** | +19.3 | 0e+00 | 44/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.85×** | +17.5 | 0e+00 | 36/37 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.66×** | +10.8 | 8e-25 | 42/43 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +6.6 | 7e-09 | 35/47 (SW480, SNU-423, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.75×** | +6.2 | 7e-08 | 38/46 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.68×** | +6.0 | 2e-07 | 36/45 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.4 | 7e-06 | 30/47 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.0 | 4e-05 | 30/44 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.84×** | +4.3 | 0.001 | 31/47 (HOP62, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.001 | 26/47 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +4.1 | 0.002 | 26/47 (HOP62, COLO 205, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.002 | 26/47 (H4, NCI-H1792, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.43×** | +4.1 | 0.002 | 26/46 (HOP62, H4, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.002 | 26/47 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.42×** | +4.0 | 0.002 | 27/46 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.007 | 27/46 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.018 | 22/46 (HOP62, NCI-H23, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.00×** | +3.4 | 0.018 | 21/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.018 | 25/46 (NCI-H460, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.019 | 24/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.88×** | +3.1 | 0.043 | 21/44 (LOX-IMVI, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.069 | 21/47 (HT-29, HOP62, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.070 | 20/47 (A549, NCI-H460, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.51×** | +2.9 | 0.079 | 18/47 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11506.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.608×** | -5.8 | 5e-06 | 31/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.724×** | -5.3 | 3e-05 | 27/47 (J82, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.654×** | -4.9 | 2e-04 | 28/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.688×** | -4.3 | 0.002 | 31/47 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.486×** | -3.6 | 0.039 | 21/47 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -3.5 | 0.047 | 23/47 (SW1417, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.689×** | -3.4 | 0.064 | 23/47 (LoVo, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.771× | -3.0 | 0.18 | 22/47 (Panc 03.27, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 51.7 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +14.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 26.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.16× (z +11.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 85.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -19.0) |
| [[KATO III (line)]] | alt | 49.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.46× (z +16.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 56.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 33.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 37.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.43× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 59.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +14.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 41.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.4× (z +18.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 63.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +14.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 58.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +14.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 45.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.95× (z +14.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 26.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.76× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 31.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.03× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +13.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 27.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.99× (z +14.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 42.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 17.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.83× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 55.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +14.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.68× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 35.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.00× (z +14.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 42.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +14.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 30.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.23× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 95.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 16.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.9× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 46.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +11.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 46.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +12.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 88.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +15.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 71.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -12.5) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.381× (z -11.8) |
| [[SW 900 (line)]] | alt | 19.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.67× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +8.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 19.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.69× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 49.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 34.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SPOPL-DT]] | +0.67 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[METTL3]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[RNASEH1]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[WDR77]] | +0.61 | +0.62 / +0.49 | both halves | 2e-05 |  |
| [[SLC25A15]] | +0.61 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[CERS2]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ADCK1]] | +0.60 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[LETM1]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[MRPS25]] | +0.59 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[PRMT3]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[WDR4]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SECISBP2L]] | -0.59 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[DBP]] | -0.59 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[RNASE4]] | -0.59 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[KBTBD7]] | -0.58 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ASB8]] | -0.57 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[GABARAP]] ⚠ | -0.56 | -0.56 / -0.38 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CTR9]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[TRAPPC5]] | -0.54 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[FAM229B]] | -0.54 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[CIR1]] | -0.53 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[TBC1D17]] | -0.53 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[TRAPPC2B]] | -0.52 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[TCEAL8]] | -0.52 | -0.52 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDM5]] | B | PRDM5 activity raises IRAK1's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.15× lower at baseline in the lines without PRDM5 | 0.021 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises IRAK1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises IRAK1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMTC4]] | C | IRAK1's natural level strengthens TMTC4's drug response | IRAK1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.01; direction clear | 0.064 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.586). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.8, -30.1); signed map (1.2, -51.5). **Vector** length 77.4, 21.4% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +6.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.0 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +4.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor associated kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,010,506-154,019,902 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IRAK, pelle |
| Gene groups (HGNC) | Interleukin 1 receptor associated kinase family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 46 pathways, smallest: TRAF6 mediated IRF7 activation in TLR7/8 or 9 signaling; IRAK1 recruits IKK complex; IRAK1 recruits IKK complex upon TLR7/8 or 9 stimulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P51617](https://www.uniprot.org/uniprotkb/P51617) (Interleukin-1 receptor-associated kinase 1):

> Serine/threonine-protein kinase that plays a critical role in initiating innate immune response against foreign pathogens. Involved in Toll-like receptor (TLR) and IL-1R signaling pathways. Is rapidly recruited by MYD88 to the receptor-signaling complex upon TLR activation. Association with MYD88 leads to IRAK1 phosphorylation by IRAK4 and subsequent autophosphorylation and kinase activation. Phosphorylates E3 ubiquitin ligases Pellino proteins (PELI1, PELI2 and PELI3) to promote …

**Summary**, from NCBI Gene [3654](https://www.ncbi.nlm.nih.gov/gene/3654):

> This gene encodes the interleukin-1 receptor-associated kinase 1, one of two putative serine/threonine kinases that become associated with the interleukin-1 receptor (IL1R) upon stimulation. This gene is partially responsible for IL1-induced upregulation of the transcription factor NF-kappa B. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6112) · Entrez [3654](https://www.ncbi.nlm.nih.gov/gene/3654) · UniProt [P51617](https://www.uniprot.org/uniprotkb/P51617) · Ensembl [ENSG00000184216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184216)

## Data

Gene col 11506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11506); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11506]; `tensor/DDL_lfc|DDL_z.npy` [11506]; `embed/gene_vectors.npy` [11506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11506 or target_col == 11506). Every well: [[IRAK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRAK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
