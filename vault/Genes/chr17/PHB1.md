---
symbol: "PHB1"
type: "gene"
col: 9411
ensembl_id: "ENSG00000167085"
name: "prohibitin 1"
location: "17q21.33"
module: 33
arm: "+"
pooled_cpm: 29.47
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# PHB1

*prohibitin 1* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.40× (z +13.4, q 3e-38, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.38× (z +4.1, q 0.002, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -8.0, q 6e-13, down in 38 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (MIA PaCa-2 0.119×, A-427 0.300×, BT-474 0.312×, Panc 03.27 0.315×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOT2]] (+0.74, fdr 7e-06), [[DLAT]] (+0.73, fdr 7e-06), [[MRPL4]] (+0.73, fdr 7e-06); moves opposite to [[TERF2IP]] (-0.67, fdr 1e-05), [[PNISR]] (-0.65, fdr 3e-05), [[TNRC6C]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **4.40×** | +13.4 | 3e-38 | 43/43 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **3.78×** | +11.6 | 2e-28 | 36/39 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.94×** | +9.0 | 4e-17 | 39/42 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **2.15×** | +6.9 | 6e-10 | 44/48 (A549, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.11×** | +6.8 | 1e-09 | 46/48 (NCI-H1792, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +6.4 | 1e-08 | 40/46 (MIA PaCa-2, J82, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.88×** | +5.7 | 9e-07 | 43/47 (A549, SW 900, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.72×** | +4.9 | 6e-05 | 31/46 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +4.5 | 4e-04 | 32/47 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 27/48 (A549, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.55×** | +3.9 | 0.004 | 24/48 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | **1.54×** | +3.8 | 0.007 | 31/47 (LoVo, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.007 | 27/47 (HOP62, SW 900, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.49×** | +3.6 | 0.014 | 25/47 (J82, A-172, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.48×** | +3.4 | 0.022 | 19/48 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.028 | 29/48 (HS-578T, SW 900, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.97×** | +3.2 | 0.043 | 22/48 (KATO III, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.045 | 22/47 (HS-578T, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.81×** | +3.0 | 0.081 | 22/46 (NCI-H460, AsPC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.87×** | +3.0 | 0.087 | 23/46 (AsPC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9411.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (MIA PaCa-2 0.119×, A-427 0.300×, BT-474 0.312×, Panc 03.27 0.315×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -8.0 | 6e-13 | 38/47 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 30.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.4) |
| [[A498 (line)]] | wt | 40.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A549 (line)]] | wt | 24.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.15× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HS-578T (line)]] | alt | 19.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[J82 (line)]] | alt | 26.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 25.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -18.1) |
| [[NCI-H1792 (line)]] | alt | 13.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.9× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.79× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SNU-423 (line)]] | alt | 20.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.42× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-427 (line)]] | wt | 48.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -12.0) |
| [[BT-474 (line)]] | alt | 97.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.9) |
| [[C-33 A (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 23.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HOP62 (line)]] | alt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Hs 766T (line)]] | wt | 22.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HT-29 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.54× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[KATO III (line)]] | alt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LoVo (line)]] | wt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.88× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H23 (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.6) |
| [[PANC-1 (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SHP-77 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 34.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -8.8) |
| [[SNU-1 (line)]] | wt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -8.8) |
| [[SW 900 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOT2]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[DLAT]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[MRPL4]] | +0.73 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[C1QBP]] | +0.71 | +0.75 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 847 |
| [[RPE]] | +0.70 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[RITA1]] | +0.70 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[MRPS27]] | +0.69 | +0.67 / +0.73 | both halves | 7e-06 | STRING 495 |
| [[NME1]] | +0.69 | +0.75 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 604 |
| [[WDR36]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CCT8]] | +0.69 | +0.72 / +0.58 | both halves | 7e-06 | STRING 421 |
| [[CDC123]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[EIPR1]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | -0.67 | -0.75 / -0.51 | both halves | 1e-05 |  |
| [[PNISR]] | -0.65 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[TNRC6C]] | -0.65 | -0.68 / -0.55 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[ZMYM5]] | -0.64 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[NFKBIB]] | -0.64 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[SMIM14]] | -0.63 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[UPF3B]] | -0.62 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.62 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[EIF1]] | -0.62 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[PABPN1]] | -0.61 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[TMEM91]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SPATC1]] | -0.59 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.2, -34.4); signed map (-10.8, -50.7). **Vector** length 78.7, 22.4% of its response variance represented; |z| ≥ 3 in 817 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.55 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.5 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +0.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.2 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.5 | -0.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.4 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | prohibitin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:49,404,049-49,414,905 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAP32; previously PHB |
| Gene groups (HGNC) | Mitochondrial nucleoid associated proteins |
| Hallmark sets | MYC_TARGETS_V2, MYC_TARGETS_V1 |
| Reactome | 13 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; RAF activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P35232](https://www.uniprot.org/uniprotkb/P35232) (Prohibitin 1):

> Protein with pleiotropic attributes mediated in a cell-compartment- and tissue-specific manner, which include the plasma membrane-associated cell signaling functions, mitochondrial chaperone, and transcriptional co-regulator of transcription factors in the nucleus. Plays a role in adipose tissue and glucose homeostasis in a sex-specific manner (By similarity). Contributes to pulmonary vascular remodeling by accelerating proliferation of pulmonary arterial smooth muscle cells (By similarity).; …

**Summary**, from NCBI Gene [5245](https://www.ncbi.nlm.nih.gov/gene/5245):

> This gene is evolutionarily conserved, and its product is proposed to play a role in human cellular senescence and tumor suppression. Antiproliferative activity is reported to be localized to the 3' UTR, which is proposed to function as a trans-acting regulatory RNA. Several pseudogenes of this gene have been identified. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:8912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8912) · Entrez [5245](https://www.ncbi.nlm.nih.gov/gene/5245) · UniProt [P35232](https://www.uniprot.org/uniprotkb/P35232) · Ensembl [ENSG00000167085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167085)

## Data

Gene col 9411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9411); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9411]; `tensor/DDL_lfc|DDL_z.npy` [9411]; `embed/gene_vectors.npy` [9411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9411 or target_col == 9411). Every well: [[PHB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
