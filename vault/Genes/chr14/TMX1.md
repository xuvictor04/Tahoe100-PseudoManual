---
symbol: "TMX1"
type: "gene"
col: 6355
ensembl_id: "ENSG00000139921"
name: "thioredoxin related transmembrane protein 1"
location: "14q22.1"
module: 29
arm: "+"
pooled_cpm: 56.21
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# TMX1

*thioredoxin related transmembrane protein 1* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.80× (z +23.3, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.23× (z +5.2, q 2e-05, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (A549 6.46×, HOP62 6.19×, NCI-H1792 5.08×, PANC-1 4.18×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (HOP62 5.49×, A549 5.46×, NCI-H460 4.49×, NCI-H1792 4.14×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.485× (z -17.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPT1]] (+0.78, fdr 7e-06), [[TGOLN2]] (+0.77, fdr 7e-06), [[MOB1A]] (+0.77, fdr 7e-06); moves opposite to [[ZFAND2B]] (-0.74, fdr 7e-06), [[SNHG32]] (-0.71, fdr 7e-06), [[CTBP1-AS]] (-0.69, fdr 7e-06, ⚠ CTBP1-AS in the vector space only through flagged drug-doses), [[ZMYM5]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6355.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (A549 6.46×, HOP62 6.19×, NCI-H1792 5.08×, PANC-1 4.18×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (HOP62 5.49×, A549 5.46×, NCI-H460 4.49×, NCI-H1792 4.14×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.80×** | +23.3 | 0e+00 | 48/48 (A549, HOP62, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +19.2 | 0e+00 | 42/42 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.10×** | +18.3 | 0e+00 | 44/45 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.2 | 2e-05 | 30/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +5.0 | 7e-05 | 23/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.485×** | -17.9 | 0e+00 | 46/48 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.628×** | -5.8 | 2e-06 | 33/48 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.741×** | -5.0 | 9e-05 | 32/48 (SW48, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.736×** | -5.0 | 1e-04 | 31/48 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.749×** | -4.8 | 1e-04 | 26/48 (RKO, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.841× | -4.3 | 0.002 | 20/48 (MIA PaCa-2, SW480, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.779×** | -4.2 | 0.002 | 24/47 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.801×** | -3.7 | 0.018 | 24/48 (HCT15, SW48, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.823×** | -3.4 | 0.045 | 20/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.818×** | -3.2 | 0.066 | 18/48 (Hs 766T, SW 1271, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.783× | -3.0 | 0.12 | 15/48 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 38.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +15.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 93.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -13.4) |
| [[HOP62 (line)]] | alt | 46.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +18.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.8) |
| [[Hs 766T (line)]] | wt | 49.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 47.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.2) |
| [[J82 (line)]] | alt | 56.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -12.9) |
| [[KATO III (line)]] | alt | 59.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.9) |
| [[LoVo (line)]] | wt | 44.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +15.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -19.2) |
| [[LS 180 (line)]] | wt | 63.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 63.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 71.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +17.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 84.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +14.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 70.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 48.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +15.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -21.0) |
| [[Panc 03.27 (line)]] | alt | 59.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.52× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -9.5) |
| [[RKO (line)]] | wt | 100 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 58.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -20.2) |
| [[SW 900 (line)]] | alt | 57.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -14.0) |
| [[SW480 (line)]] | alt | 74.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.607× (z -8.5) |
| [[A-427 (line)]] | wt | 54.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0747× (z -24.1) |
| [[A549 (line)]] | wt | 54.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.46× (z +19.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 31.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.3) |
| [[C32 (line)]] | wt | 46.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +14.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 60.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +14.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -9.1) |
| [[HS-578T (line)]] | alt | 35.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.61× (z +14.3) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 31.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +11.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 58.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 40.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +14.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 74.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -9.3) |
| [[PANC-1 (line)]] | alt | 50.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +16.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 46.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -8.5) |
| [[SNU-423 (line)]] | alt | 38.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +13.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 34.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +8.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 55.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 88.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.6) |
| [[SHP-77 (line)]] | alt | 79.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 54.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -8.5) |
| [[SW1417 (line)]] | alt | 43.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -9.6) |
| [[SW48 (line)]] | wt | 68.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.9) |
| [[C-33 A (line)]] | alt | 72.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 51.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.91× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 62.4 | 0 | 1 | — | [[Rucaparib (phosphate) (drug)]] 0.5 µM 0.0702× (z -8.8) |
| [[AN3 CA (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | +0.78 | +0.75 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[TGOLN2]] | +0.77 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[FUCA2]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[MMGT1]] | +0.73 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[RBBP7]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[PGRMC1]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.70 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[RPE]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[NONO]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[EIF4H]] | +0.69 | +0.51 / +0.76 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAND2B]] | -0.74 | -0.65 / -0.75 | both halves | 7e-06 |  |
| [[SNHG32]] | -0.71 | -0.69 / -0.68 | both halves | 7e-06 |  |
| [[CTBP1-AS]] ⚠ | -0.69 | -0.67 / -0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ZMYM5]] | -0.69 | -0.63 / -0.72 | both halves | 7e-06 |  |
| [[WASHC1]] | -0.68 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[SNHG8]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[LINC00685]] | -0.67 | -0.56 / -0.75 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.67 | -0.61 / -0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NFKBIL1]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[EPB41L4A-AS1]] | -0.66 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[ACAP1]] | -0.65 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[ATF4]] | -0.65 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[NSUN5P1-1]] | -0.65 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[ZNF316]] | -0.64 | -0.64 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.784). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-28.5, -22.0); signed map (-21.1, -38.2). **Vector** length 118, 33.1% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.7 | +5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +19.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +1.4 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +3.0 | +1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.8 | +1.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.7 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.2 | -17.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -6.4 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -5.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.8 | -3.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.8 | -1.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.7 | -3.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -3.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin related transmembrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:51,240,162-51,257,655 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TMX, PDIA11; previously TXNDC, TXNDC1 |
| Gene groups (HGNC) | Protein disulfide isomerases; Thioredoxin domain containing |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3N1](https://www.uniprot.org/uniprotkb/Q9H3N1) (Thioredoxin-related transmembrane protein 1):

> Thioredoxin domain-containing protein that participates in various redox reactions through the reversible oxidation of its active center dithiol to a disulfide and catalyze dithiol-disulfide exchange reactions. Acts as a key inhibitor of the alternative triglyceride biosynthesis pathway by inhibiting the activity of TMEM68/DIESL at the endoplasmic reticulum, thereby restricting accumulation of triacylglycerol. The alternative triglyceride biosynthesis pathway mediates formation of …

**Summary**, from NCBI Gene [81542](https://www.ncbi.nlm.nih.gov/gene/81542):

> This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, a catalytically active thioredoxin domain, and one transmembrane domain. Unlike most members of this gene family, it lacks a C-terminal ER-retention sequence. The mature membrane-bound protein can both oxidize and reduce disulfide bonds and acts selectively on …

**Accessions** — [HGNC:15487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15487) · Entrez [81542](https://www.ncbi.nlm.nih.gov/gene/81542) · UniProt [Q9H3N1](https://www.uniprot.org/uniprotkb/Q9H3N1) · Ensembl [ENSG00000139921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139921)

## Data

Gene col 6355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6355); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6355]; `tensor/DDL_lfc|DDL_z.npy` [6355]; `embed/gene_vectors.npy` [6355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6355 or target_col == 6355). Every well: [[TMX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
