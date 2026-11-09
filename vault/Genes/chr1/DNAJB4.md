---
symbol: "DNAJB4"
type: "gene"
col: 8544
ensembl_id: "ENSG00000162616"
name: "DnaJ heat shock protein family (Hsp40) member B4"
location: "1p31.1"
module: 135
arm: "+"
pooled_cpm: 21.28
n_lines_expressing: 48
n_dd_up: 37
n_dd_down: 3
n_dd_up_clean: 33
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# DNAJB4

*DnaJ heat shock protein family (Hsp40) member B4* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.10× (z +34.6, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.697× (z -5.2, q 9e-05, down in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HT-29 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (SHP-77 0.102×); [[Menadione (drug)]] 0.05 µM in 1 line (BT-474 0.0808×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (C32 0.160×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HTATIP2]] (+0.68, fdr 1e-05), [[GIPC2]] (+0.67, fdr 1e-05, ⚠ same locus), [[CCDC117]] (+0.67, fdr 1e-05), [[HSPB1]] (+0.66, fdr 7e-06); moves opposite to [[PACS2]] (-0.63, fdr 1e-05), [[BORCS5]] (-0.61, fdr 1e-05), [[TXNL4A]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.10×** | +34.6 | 0e+00 | 44/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.62×** | +23.0 | 0e+00 | 46/46 (C32, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **4.40×** | +21.4 | 0e+00 | 42/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.83×** | +20.1 | 0e+00 | 46/46 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.56×** | +18.0 | 0e+00 | 45/46 (A498, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.68×** | +16.8 | 0e+00 | 44/46 (A498, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.03×** | +16.6 | 0e+00 | 41/45 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +16.0 | 0e+00 | 41/45 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.89×** | +12.5 | 8e-34 | 39/39 (RPMI-7951, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.98×** | +10.2 | 8e-23 | 34/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.56×** | +10.1 | 4e-22 | 40/46 (A498, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +9.2 | 2e-18 | 35/46 (NCI-H23, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +8.5 | 6e-16 | 31/46 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM |  | **2.85×** | +8.2 | 9e-15 | 33/45 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **2.79×** | +8.1 | 3e-14 | 38/45 (HS-578T, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +8.0 | 5e-14 | 31/45 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8544.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HT-29 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (SHP-77 0.102×); [[Menadione (drug)]] 0.05 µM in 1 line (BT-474 0.0808×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (C32 0.160×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.697×** | -5.2 | 9e-05 | 21/46 (RPMI-7951, LOX-IMVI, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.662×** | -4.4 | 0.002 | 20/43 (A498, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.767×** | -4.0 | 0.011 | 19/46 (NCI-H460, RKO, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.741× | -3.2 | 0.17 | 12/46 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.812× | -3.2 | 0.17 | 8/46 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.819× | -3.0 | 0.20 | 14/45 (NCI-H2030, J82, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.819× | -3.0 | 0.20 | 15/38 (A-427, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +15.9) | — |
| [[A498 (line)]] | wt | 55.3 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +21.1) | — |
| [[HEC-1-A (line)]] | alt | 18.7 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +17.8) | — |
| [[NCI-H460 (line)]] | wt | 23.2 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +24.4) | — |
| [[PANC-1 (line)]] | alt | 19.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +22.2) | — |
| [[C32 (line)]] | wt | 18.4 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +15.8) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.160× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +19.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +16.8) | — |
| [[A-427 (line)]] | wt | 23.7 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 13.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.16× (z +16.4) | — |
| [[RKO (line)]] | wt | 20.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 30.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +17.8) | — |
| [[HT-29 (line)]] | alt | 33.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +17.4) | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[KATO III (line)]] | alt | 17.1 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.57× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 40.1 | 5 | 0 | [[Bortezomib (drug)]] 0.05 µM 5.15× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 25.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +20.1) | — |
| [[A549 (line)]] | wt | 9.72 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +17.9) | — |
| [[NCI-H2030 (line)]] | alt | 30.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +11.6) | — |
| [[SW480 (line)]] | alt | 16.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.43× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 9.80 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 28.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +13.4) | — |
| [[LoVo (line)]] | wt | 11.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 20.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +15.7) | — |
| [[RPMI-7951 (line)]] | alt | 33.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.16× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 17.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +15.0) | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +14.5) | — |
| [[BT-474 (line)]] | alt | 10.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +9.6) | [[Menadione (drug)]] 0.05 µM 0.0808× (z -10.0) |
| [[C-33 A (line)]] | alt | 25.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +9.3) | — |
| [[J82 (line)]] | alt | 37.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +17.7) | — |
| [[NCI-H23 (line)]] | alt | 23.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.15× (z +19.5) | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 30.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +14.8) | — |
| [[H4 (line)]] | wt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.102× (z -11.5) |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HTATIP2]] | +0.68 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[GIPC2]] | +0.67 | +0.72 / +0.50 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CCDC117]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[HSPB1]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 | STRING 403 |
| [[CAPS2]] | +0.62 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[SOD1]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TDP2]] | +0.60 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[ABCC2]] | +0.59 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[BAG2]] | +0.59 | +0.59 / +0.40 | both halves | 5e-05 | STRING 783 |
| [[UBB]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[UBXN4]] | +0.59 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[RNF6]] | +0.59 | +0.64 / +0.38 | both halves | 6e-05 |  |
| [[RNASEL]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACS2]] | -0.63 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[BORCS5]] | -0.61 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[TXNL4A]] | -0.59 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[NUP93]] | -0.56 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[TATDN2]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ATP13A3]] | -0.56 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[RASA2]] | -0.55 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[BRAT1]] | -0.55 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[SSBP4]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SFI1]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[WDR5]] | -0.54 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[TRIM35]] | -0.54 | -0.52 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DNAJB4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[USP31]] | C | USP31 activity raises DNAJB4's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.64× lower at baseline in the lines without USP31 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (14.0, -8.5); signed map (7.6, -29.5). **Vector** length 111, 30.8% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.1 | +23.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.1 | +18.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.0 | +16.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +20.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.0 | +12.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +4.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.2 | +3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +4.4 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | +0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.5 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member B4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:77,979,175-78,017,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HLJ1 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UDY4](https://www.uniprot.org/uniprotkb/Q9UDY4) (DnaJ homolog subfamily B member 4):

> Probable chaperone. Stimulates ATP hydrolysis and the folding of unfolded proteins mediated by HSPA1A/B (in vitro).

**Summary**, from NCBI Gene [11080](https://www.ncbi.nlm.nih.gov/gene/11080):

> The protein encoded by this gene is a molecular chaperone, tumor suppressor, and member of the heat shock protein-40 family. The encoded protein binds the cell adhesion protein E-cadherin and targets it to the plasma membrane. This protein also binds incorrectly folded E-cadherin and targets it for endoplasmic reticulum-associated degradation. This gene is a strong tumor suppressor for colorectal carcinoma, and downregulation of it may serve as a good biomarker for predicting patient outcomes. …

**Accessions** — [HGNC:14886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14886) · Entrez [11080](https://www.ncbi.nlm.nih.gov/gene/11080) · UniProt [Q9UDY4](https://www.uniprot.org/uniprotkb/Q9UDY4) · Ensembl [ENSG00000162616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162616)

## Data

Gene col 8544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8544); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8544]; `tensor/DDL_lfc|DDL_z.npy` [8544]; `embed/gene_vectors.npy` [8544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8544 or target_col == 8544). Every well: [[DNAJB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
