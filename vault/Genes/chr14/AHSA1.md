---
symbol: "AHSA1"
type: "gene"
col: 1992
ensembl_id: "ENSG00000100591"
name: "activator of HSP90 ATPase activity 1"
location: "14q24.3"
module: 60
arm: "+"
pooled_cpm: 35.13
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# AHSA1

*activator of HSP90 ATPase activity 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (25 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.82× (z +21.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.704× (z -6.9, q 3e-09, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.276×, NCI-H2030 0.473×, RKO 0.418×, C-33 A 0.359×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.264×, MIA PaCa-2 0.215×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.677×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA8]] (+0.81, fdr 7e-06), [[TCP1]] (+0.76, fdr 7e-06), [[CACYBP]] (+0.75, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.68, fdr 7e-06), [[RELB]] (-0.67, fdr 7e-06), [[PIM3]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BHLHE41]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 26 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1992.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.82×** | +21.7 | 0e+00 | 48/48 (HOP62, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.36×** | +20.3 | 0e+00 | 47/47 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.61×** | +16.7 | 0e+00 | 48/48 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **4.20×** | +15.8 | 0e+00 | 47/48 (A498, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.80×** | +13.6 | 3e-40 | 45/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.52×** | +12.7 | 3e-35 | 38/45 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.54×** | +12.3 | 5e-33 | 34/39 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.19×** | +10.3 | 4e-23 | 43/43 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.04×** | +9.1 | 6e-18 | 35/43 (NCI-H23, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.42×** | +8.7 | 2e-16 | 41/48 (CFPAC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.54×** | +8.4 | 3e-15 | 33/48 (NCI-H2030, NCI-H1792, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +7.9 | 1e-13 | 38/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.73×** | +7.5 | 2e-12 | 33/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.70×** | +7.0 | 9e-11 | 37/48 (SK-MEL-2, HS-578T, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.66×** | +6.9 | 2e-10 | 33/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +6.1 | 3e-08 | 29/48 (A549, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **2.29×** | +6.0 | 7e-08 | 39/46 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **2.17×** | +5.6 | 7e-07 | 37/48 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.5 | 1e-04 | 22/48 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 1e-04 | 26/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 5e-04 | 17/48 (HOP62, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.001 | 23/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.001 | 24/47 (Hs 766T, SW 900, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +3.9 | 0.002 | 25/48 (CFPAC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.002 | 18/48 (CFPAC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1992.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.276×, NCI-H2030 0.473×, RKO 0.418×, C-33 A 0.359×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.264×, MIA PaCa-2 0.215×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.677×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.704×** | -6.9 | 3e-09 | 32/48 (A-427, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.761×** | -3.7 | 0.073 | 24/48 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -3.5 | 0.090 | 20/48 (Hs 766T, SW1417, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.845× | -3.2 | 0.16 | 15/48 (NCI-H23, LoVo, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1992. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.6 | 8 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.18× (z +11.3) | — |
| [[SW480 (line)]] | alt | 44.0 | 7 (4 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 5.88× (z +17.4) | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -8.9) |
| [[HOP62 (line)]] | alt | 21.1 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 13.0× (z +18.4) | — |
| [[PANC-1 (line)]] | alt | 22.5 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.88× (z +14.6) | — |
| [[A498 (line)]] | wt | 32.0 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.89× (z +14.1) | — |
| [[A549 (line)]] | wt | 28.4 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.58× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.53× (z +14.8) | — |
| [[A-427 (line)]] | wt | 54.5 | 3 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.52× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 27.2 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.10× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 18.4 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.67× (z +14.8) | — |
| [[LoVo (line)]] | wt | 39.5 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.90× (z +17.1) | — |
| [[LS 180 (line)]] | wt | 34.2 | 5 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.33× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.13× (z +15.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 79.0 | 4 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.38× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 35.3 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.27× (z +12.4) | — |
| [[A-172 (line)]] | wt | 15.8 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.28× (z +13.4) | — |
| [[Hs 766T (line)]] | wt | 20.1 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.88× (z +11.9) | — |
| [[J82 (line)]] | alt | 32.7 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.43× (z +10.7) | — |
| [[KATO III (line)]] | alt | 35.2 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.57× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 22.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2347 (line)]] | alt | 52.8 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.66× (z +13.4) | — |
| [[RKO (line)]] | wt | 55.7 | 3 | 1 | [[Auranofin (drug)]] 5 µM 6.60× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.0) |
| [[SW1417 (line)]] | alt | 43.5 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.81× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 30.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.36× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 26.2 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.55× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 22.4 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.18× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 41.4 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.32× (z +12.5) | — |
| [[BT-474 (line)]] | alt | 41.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.72× (z +13.7) | — |
| [[C-33 A (line)]] | alt | 43.4 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.34× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.4) |
| [[C32 (line)]] | wt | 22.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 19.9× (z +16.6) | — |
| [[HCT15 (line)]] | alt | 35.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.82× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.05× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 31.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.61× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 64.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.05× (z +13.0) | — |
| [[SNU-423 (line)]] | alt | 18.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 9.27× (z +12.4) | — |
| [[SW 900 (line)]] | alt | 36.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.36× (z +12.3) | — |
| [[AN3 CA (line)]] | alt | 45.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.17× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 27.6× (z +14.4) ⚠ toxic | — |
| [[H4 (line)]] | wt | 25.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.90× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 56.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.68× (z +11.1) | — |
| [[SNU-1 (line)]] | wt | 31.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.4× (z +12.8) | — |
| [[SW48 (line)]] | wt | 71.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.62× (z +10.5) | — |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1992), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA8]] | +0.81 | +0.85 / +0.79 | both halves | 7e-06 | STRING 930 |
| [[TCP1]] | +0.76 | +0.70 / +0.78 | both halves | 7e-06 | STRING 529 |
| [[CACYBP]] | +0.75 | +0.77 / +0.70 | both halves | 7e-06 | STRING 730 |
| [[FKBP4]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 | STRING 973 |
| [[CHORDC1]] | +0.74 | +0.68 / +0.76 | both halves | 7e-06 | STRING 858 |
| [[CCT3]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 | STRING 675 |
| [[HSPD1]] | +0.72 | +0.76 / +0.70 | both halves | 7e-06 | STRING 782 |
| [[ATP2C1]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[HSPE1]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 | STRING 831 |
| [[NAA50]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[GPN1]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[SERPINH1]] | +0.71 | +0.69 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.68 | -0.74 / -0.64 | both halves | 7e-06 |  |
| [[RELB]] | -0.67 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[PIM3]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[ANKRD12]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[NBPF19]] | -0.67 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[HCFC2]] | -0.66 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[DOP1A]] | -0.65 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[TXNIP]] | -0.65 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[POGZ]] | -0.65 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[CCDC148]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[KMT5B]] | -0.63 | -0.61 / -0.57 | both halves | 8e-06 |  |
| [[TMEM205]] | -0.63 | -0.67 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BHLHE41]] | B | BHLHE41 activity lowers AHSA1's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.37× higher at baseline in the lines without BHLHE41 | 0.028 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[TOP2A]] | B | TOP2A activity lowers AHSA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FOXA2]] | B | FOXA2 activity lowers AHSA1's level | lines that do not express FOXA2 (28) vs lines expressing it (22) | 1.26× higher at baseline in the lines without FOXA2 | 0.078 | ⚠ within organs, on part of the lines; also absent: TFF1, GPX2, F5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.7, -11.3); signed map (-26.6, -29.4). **Vector** length 109, 35.2% of its response variance represented; |z| ≥ 3 in 1,345 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.51 to 13); *Attenuation phase* (reactome, mean cos +0.52 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.50 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.5 | +21.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.5 | +16.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.4 | +20.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +15.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +8.0 | +10.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.4 | +5.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.4 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.8 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.2 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.5 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | activator of HSP90 ATPase activity 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,457,870-77,469,472 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p38, Aha1, hAha1; previously C14orf3 |
| Matched by | ensembl_id |

**Function**, from UniProt [O95433](https://www.uniprot.org/uniprotkb/O95433) (Activator of 90 kDa heat shock protein ATPase homolog 1):

> Acts as a co-chaperone of HSP90AA1. Activates the ATPase activity of HSP90AA1 leading to increase in its chaperone activity. Competes with the inhibitory co-chaperone FNIP1 for binding to HSP90AA1, thereby providing a reciprocal regulatory mechanism for chaperoning of client proteins. Competes with the inhibitory co-chaperone TSC1 for binding to HSP90AA1, thereby providing a reciprocal regulatory mechanism for chaperoning of client proteins.

**Summary**, from NCBI Gene [10598](https://www.ncbi.nlm.nih.gov/gene/10598):

> Enables several functions, including Hsp90 protein binding activity; protein folding chaperone; and unfolded protein binding activity. Involved in maintenance of unfolded protein and positive regulation of ATP-dependent activity. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1189) · Entrez [10598](https://www.ncbi.nlm.nih.gov/gene/10598) · UniProt [O95433](https://www.uniprot.org/uniprotkb/O95433) · Ensembl [ENSG00000100591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100591)

## Data

Gene col 1992: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1992); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1992, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1992]; `tensor/DDL_lfc|DDL_z.npy` [1992]; `embed/gene_vectors.npy` [1992]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1992 or target_col == 1992). Every well: [[AHSA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHSA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
