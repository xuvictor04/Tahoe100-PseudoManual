---
symbol: "IRF1"
type: "gene"
col: 4602
ensembl_id: "ENSG00000125347"
name: "interferon regulatory factor 1"
location: "5q31.1"
module: 14
arm: "+"
pooled_cpm: 106.08
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 26
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# IRF1

*interferon regulatory factor 1* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.45× (z +35.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.729× (z -5.2, q 9e-05, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP2]] (+0.76, fdr 7e-06), [[BCL3]] (+0.73, fdr 7e-06), [[REL]] (+0.72, fdr 7e-06); moves opposite to [[POP1]] (-0.56, fdr 1e-05), [[THOC5]] (-0.54, fdr 1e-05), [[HERC2P3]] (-0.54, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[CTSS]] → it (grade B ⚠); 2 go from it, the strongest it → [[PSMB9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.45×** | +35.6 | 0e+00 | 48/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **7.89×** | +23.4 | 0e+00 | 47/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.05×** | +16.5 | 0e+00 | 46/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +16.1 | 0e+00 | 46/49 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.35×** | +10.1 | 6e-22 | 36/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.73×** | +9.6 | 9e-20 | 47/49 (Panc 03.27, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.00×** | +8.2 | 2e-14 | 33/48 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +8.1 | 5e-14 | 33/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.70×** | +6.2 | 3e-08 | 29/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.74×** | +6.1 | 8e-08 | 28/45 (H4, J82, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +5.7 | 7e-07 | 35/48 (LS 180, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +5.0 | 3e-05 | 32/48 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.003 | 27/49 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.39×** | +3.7 | 0.008 | 26/50 (NCI-H460, RKO, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.016 | 21/49 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.072 | 13/48 (NCI-H2347, A549, …) | rises with dose | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.100 | 15/49 (H4, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.729×** | -5.2 | 9e-05 | 33/49 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.435×** | -5.1 | 9e-05 | 35/47 (SHP-77, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.800×** | -3.7 | 0.035 | 25/49 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.722×** | -3.6 | 0.035 | 24/48 (HT-29, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -3.6 | 0.035 | 24/48 (AsPC-1, HT-29, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.567×** | -3.5 | 0.046 | 24/48 (LoVo, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.752×** | -3.3 | 0.068 | 24/49 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.832× | -3.0 | 0.16 | 18/48 (LoVo, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 51.0 | 14 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +25.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 92.7 | 8 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 9.42× (z +23.9) | [[Tofacitinib (drug)]] 5 µM 0.366× (z -10.7) |
| [[PANC-1 (line)]] | alt | 75.4 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +39.4) | — |
| [[J82 (line)]] | alt | 95.2 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +27.4) | — |
| [[NCI-H2347 (line)]] | alt | 129 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +20.7) | [[Auranofin (drug)]] 5 µM 0.273× (z -10.3) |
| [[SW48 (line)]] | wt | 59.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +20.4) | — |
| [[A-172 (line)]] | wt | 145 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +24.2) | — |
| [[A549 (line)]] | wt | 158 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +26.7) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 69.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +19.3) | — |
| [[HEC-1-A (line)]] | alt | 137 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +30.0) | — |
| [[HOP62 (line)]] | alt | 62.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +28.5) | — |
| [[HS-578T (line)]] | alt | 218 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +24.9) | — |
| [[hTERT-HPNE (line)]] | wt | 88.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.7× (z +24.8) | — |
| [[LS 180 (line)]] | wt | 44.6 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +20.1) | — |
| [[NCI-H1792 (line)]] | alt | 86.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.72× (z +24.9) | — |
| [[Panc 03.27 (line)]] | alt | 163 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +29.5) | [[Auranofin (drug)]] 5 µM 0.346× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 56.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +23.7) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 164 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +29.5) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 40.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.2× (z +22.0) | — |
| [[HT-29 (line)]] | alt | 227 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.303× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 128 | 5 | 0 | [[Harringtonine (drug)]] 5 µM 18.6× (z +20.1) | — |
| [[SNU-1 (line)]] | wt | 52.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +18.7) | — |
| [[SW 900 (line)]] | alt | 93.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +18.2) | — |
| [[AsPC-1 (line)]] | alt | 130 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +20.6) | [[Auranofin (drug)]] 5 µM 0.179× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 177 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +25.7) | — |
| [[HCT15 (line)]] | alt | 55.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +15.4) | — |
| [[KATO III (line)]] | alt | 110 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +12.0) | [[Auranofin (drug)]] 5 µM 0.211× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 132 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.0526× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 49.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +16.0) | — |
| [[AN3 CA (line)]] | alt | 79.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +13.9) | — |
| [[BT-474 (line)]] | alt | 112 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +21.5) | — |
| [[HepG2_C3A (line)]] | wt | 80.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +20.2) | — |
| [[Hs 766T (line)]] | wt | 188 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +18.7) | [[Auranofin (drug)]] 5 µM 0.280× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 31.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +20.6) | — |
| [[NCI-H2030 (line)]] | alt | 50.1 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 18.5× (z +16.2) | — |
| [[SNU-423 (line)]] | alt | 111 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +31.5) | — |
| [[SW 1088 (line)]] | alt | 186 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 129 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +19.3) | — |
| [[SW480 (line)]] | alt | 64.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +20.7) | — |
| [[LoVo (line)]] | wt | 204 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +16.5) | [[Tofacitinib (drug)]] 5 µM 0.383× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 70.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.9) | — |
| [[RKO (line)]] | wt | 51.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 48.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +12.2) | — |
| [[C-33 A (line)]] | alt | 54.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 67.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +11.8) | — |
| [[SW 1271 (line)]] | alt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP2]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[BCL3]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 545 |
| [[REL]] | +0.72 | +0.73 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 713 |
| [[CCNL1]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PSMB9]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT; STRING 875 |
| [[EFNA1]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NFKBIA]] | +0.67 | +0.72 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 681 |
| [[CCL5]] | +0.66 | +0.58 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT; STRING 728 |
| [[B2M]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 581 |
| [[HLA-F]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP; STRING 523 |
| [[MAP3K8]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING |
| [[TAP1]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS; STRING 821 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP1]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[THOC5]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[HERC2P3]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 26, C 0. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | CTSS activity raises IRF1's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.94× lower at baseline in the lines without CTSS | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises IRF1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without GBP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[GBP4]] | B | GBP4 activity raises IRF1's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without GBP4 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[TNFAIP2]] | B | TNFAIP2 activity raises IRF1's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without TNFAIP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[FBXO39]] | B | FBXO39 activity raises IRF1's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without FBXO39 | 0.014 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[CXCL3]] | B | CXCL3 activity raises IRF1's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without CXCL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[CD74]] | B | CD74 activity raises IRF1's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.36× lower at baseline in the lines without CD74 | 0.019 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[RHOV]] | B | RHOV activity raises IRF1's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.60× lower at baseline in the lines without RHOV | 0.020 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[OAS1]] | B | OAS1 activity raises IRF1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without OAS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[TNFSF10]] | B | TNFSF10 activity raises IRF1's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 1.75× lower at baseline in the lines without TNFSF10 | 0.028 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[TSPAN15]] | B | TSPAN15 activity raises IRF1's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without TSPAN15 | 0.032 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[ELF3]] | B | ELF3 activity raises IRF1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.41× lower at baseline in the lines without ELF3 | 0.038 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB9]] | C | IRF1's natural level strengthens PSMB9's drug response | IRF1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.73, reverse -0.32; direction not clear | 0.008 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[BTN3A1]] | C | IRF1's natural level strengthens BTN3A1's drug response | IRF1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.26; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, 4.4); signed map (44.5, 6.7). **Vector** length 145, 53.7% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.59 to 12); *IkBA variant leads to EDA-ID* (reactome, mean cos +0.51 to 4); *Toll Like Receptor 3 (TLR3) Cascade* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +23.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.2 | +3.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.3 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +1.3 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | +3.5 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.5 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.8 | -1.8 |
|  | [[NG25 (drug)]] 5 µM |  | -7.7 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | -7.6 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -7.4 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.7 | -1.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.0 | -5.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | interferon regulatory factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,440,440-132,508,719 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAR |
| Gene groups (HGNC) | Interferon regulatory factors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INTERFERON_ALPHA_RESPONSE, INFLAMMATORY_RESPONSE, APOPTOSIS, UV_RESPONSE_UP, COMPLEMENT, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 16 pathways, smallest: Pyroptosis; Regulated Necrosis; Regulation of PD-L1(CD274) transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P10914](https://www.uniprot.org/uniprotkb/P10914) (Interferon regulatory factor 1):

> Transcriptional regulator which displays a remarkable functional diversity in the regulation of cellular responses. Regulates transcription of IFN and IFN-inducible genes, host response to viral and bacterial infections, regulation of many genes expressed during hematopoiesis, inflammation, immune responses and cell proliferation and differentiation, regulation of the cell cycle and induction of growth arrest and programmed cell death following DNA damage. Stimulates both innate and acquired …

**Summary**, from NCBI Gene [3659](https://www.ncbi.nlm.nih.gov/gene/3659):

> The protein encoded by this gene is a transcriptional regulator and tumor suppressor, serving as an activator of genes involved in both innate and acquired immune responses. The encoded protein activates the transcription of genes involved in the body's response to viruses and bacteria, playing a role in cell proliferation, apoptosis, the immune response, and DNA damage response. This protein represses the transcription of several other genes. As a tumor suppressor, it both suppresses tumor …

**Accessions** — [HGNC:6116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6116) · Entrez [3659](https://www.ncbi.nlm.nih.gov/gene/3659) · UniProt [P10914](https://www.uniprot.org/uniprotkb/P10914) · Ensembl [ENSG00000125347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125347)

## Data

Gene col 4602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4602); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4602]; `tensor/DDL_lfc|DDL_z.npy` [4602]; `embed/gene_vectors.npy` [4602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4602 or target_col == 4602). Every well: [[IRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
