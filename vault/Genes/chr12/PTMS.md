---
symbol: "PTMS"
type: "gene"
col: 8245
ensembl_id: "ENSG00000159335"
name: "parathymosin"
location: "12p13.31"
module: 1
arm: "-"
pooled_cpm: 89.41
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PTMS

*parathymosin* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.12× (z +16.8, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +3.6, q 0.023, up in 29 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HOP62 7.68×, PANC-1 6.16×, SW480 5.60×, NCI-H1573 8.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 6.00×, PANC-1 6.31×, HOP62 7.55×, A549 7.79×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 2.00×, A498 2.14×).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.684× (z -6.0, q 2e-06, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAS]] (+0.59, fdr 1e-05), [[SUMO2]] (+0.57, fdr 3e-05), [[TLE5]] (+0.57, fdr 1e-05); moves opposite to [[DNAJA3]] (-0.57, fdr 1e-05), [[MYG1]] (-0.55, fdr 4e-05), [[EIF6]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8245.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HOP62 7.68×, PANC-1 6.16×, SW480 5.60×, NCI-H1573 8.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 6.00×, PANC-1 6.31×, HOP62 7.55×, A549 7.79×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 2.00×, A498 2.14×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.12×** | +16.8 | 0e+00 | 48/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.39×** | +15.8 | 0e+00 | 44/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +12.3 | 3e-32 | 44/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **2.04×** | +7.9 | 4e-13 | 46/47 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.70×** | +5.9 | 5e-07 | 41/47 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.9 | 9e-05 | 33/46 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.41×** | +3.6 | 0.022 | 27/46 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.023 | 29/49 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.1 | 0.11 | 25/48 (NCI-H2347, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.22× | +3.1 | 0.12 | 22/47 (Panc 03.27, CFPAC-1, …) | rises with dose | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.31× | +3.0 | 0.12 | 26/47 (C32, HS-578T, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.31× | +3.0 | 0.12 | 23/47 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8245.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.684×** | -6.0 | 2e-06 | 30/47 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.624×** | -5.2 | 5e-05 | 36/47 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.637×** | -5.0 | 1e-04 | 33/47 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.650×** | -4.8 | 2e-04 | 31/47 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.687×** | -4.2 | 0.004 | 34/47 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.719× | -3.0 | 0.24 | 23/47 (SNU-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 82.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +10.4) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.254× (z -11.0) |
| [[SW480 (line)]] | alt | 146 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.00× (z +16.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.4) |
| [[A498 (line)]] | wt | 73.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 103 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.55× (z +16.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 34.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.61× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 121 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +13.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 83.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.31× (z +16.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 77.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 364 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -18.8) |
| [[C-33 A (line)]] | alt | 87.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -12.1) |
| [[C32 (line)]] | wt | 191 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.322× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 35.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 48.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.58× (z +14.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +14.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 65.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.10× (z +14.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 80.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +14.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 59.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.11× (z +13.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 52.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.06× (z +14.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 63.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.60× (z +15.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 47.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.36× (z +14.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 117 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 46.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.46× (z +14.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 78.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +12.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 43.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 9.74× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 101 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 60.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.04× (z +12.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 100 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.79× (z +15.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 40.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.86× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 43.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.79× (z +10.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 61.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.88× (z +10.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 242 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +14.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 85.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 43.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 74.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.32× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 97.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 157 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.216× (z -9.3) |
| [[H4 (line)]] | wt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 61.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 144 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -11.1) |
| [[SW 1088 (line)]] | alt | 106 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0921× (z -8.8) |
| [[SW1417 (line)]] | alt | 76.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +10.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SUMO2]] | +0.57 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[TLE5]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CDK2AP1]] | +0.57 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[LDB1]] | +0.55 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[NLGN2]] | +0.54 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[COL3A1]] | +0.53 | +0.47 / +0.38 | both halves | 7e-05 |  |
| [[USF2]] | +0.53 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[PABPN1]] | +0.52 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[EMC10]] | +0.52 | +0.39 / +0.45 | both halves | 6e-05 |  |
| [[DBI]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[PRRT2]] | +0.51 | +0.38 / +0.44 | both halves | 6e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJA3]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[MYG1]] | -0.55 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[EIF6]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[VPS25]] | -0.53 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[FAN1]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[NSUN5]] | -0.53 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[BCS1L]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[HAUS7]] | -0.52 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[RPUSD3]] | -0.51 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[DRG2]] | -0.51 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[RPP40]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TATDN1]] | -0.50 | -0.59 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PTMS's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NLGN2]] | C | NLGN2 activity raises PTMS's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without NLGN2 | 0.0997 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.362). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.5, -48.2); signed map (-23.6, -5.3). **Vector** length 94.1, 32.3% of its response variance represented; |z| ≥ 3 in 808 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.0 | +5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +1.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +2.9 | -0.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.7 | +0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | -3.6 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.7 | +1.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.2 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | parathymosin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,765,516-6,770,952 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ParaT |
| Matched by | ensembl_id |

**Function**, from UniProt [P20962](https://www.uniprot.org/uniprotkb/P20962) (Parathymosin):

> Parathymosin may mediate immune function by blocking the effect of prothymosin alpha which confers resistance to certain opportunistic infections.

**Summary**, from NCBI Gene [5763](https://www.ncbi.nlm.nih.gov/gene/5763):

> Predicted to enable histone binding activity. Predicted to be involved in negative regulation of apoptotic process and positive regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9629) · Entrez [5763](https://www.ncbi.nlm.nih.gov/gene/5763) · UniProt [P20962](https://www.uniprot.org/uniprotkb/P20962) · Ensembl [ENSG00000159335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159335)

## Data

Gene col 8245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8245); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8245]; `tensor/DDL_lfc|DDL_z.npy` [8245]; `embed/gene_vectors.npy` [8245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8245 or target_col == 8245). Every well: [[PTMS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTMS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
