---
symbol: "DLGAP4"
type: "gene"
col: 1296
ensembl_id: "ENSG00000080845"
name: "DLG associated protein 4"
location: "20q11.23"
module: 189
arm: "+"
pooled_cpm: 126.75
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# DLGAP4

*DLG associated protein 4* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.55× (z +9.8, q 8e-20, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.660× (z -13.5, q 5e-39, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDLIM7]] (+0.70, fdr 7e-06), [[RAP1B]] (+0.67, fdr 8e-06), [[TMEM184B]] (+0.66, fdr 1e-05); moves opposite to [[ECHDC1]] (-0.61, fdr 3e-05), [[COPS8-DT]] (-0.59, fdr 1e-05), [[RBBP4]] (-0.58, fdr 1e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SYT7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.55×** | +9.8 | 8e-20 | 33/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.38×** | +7.5 | 3e-11 | 35/47 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +7.3 | 6e-11 | 26/48 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +5.5 | 7e-06 | 26/48 (SW1417, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +5.4 | 8e-06 | 20/49 (LS 180, SHP-77, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +5.0 | 5e-05 | 25/48 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +4.8 | 1e-04 | 25/48 (LS 180, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.20×** | +4.2 | 0.002 | 19/48 (SW1417, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.2 | 0.002 | 18/48 (SW1417, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.002 | 23/48 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.045 | 12/47 (A-172, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.056 | 20/48 (SW1417, A-427, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.14× | +3.0 | 0.10 | 17/47 (LS 180, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -13.5 | 5e-39 | 39/49 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.668×** | -8.6 | 3e-15 | 29/45 (C32, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.729×** | -7.3 | 6e-11 | 33/49 (Panc 03.27, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -7.2 | 7e-11 | 27/48 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.726×** | -7.1 | 2e-10 | 29/44 (HCT15, NCI-H460, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.608×** | -6.0 | 2e-07 | 31/49 (HOP62, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.768×** | -5.8 | 4e-07 | 29/47 (NCI-H2030, Hs 766T, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.619×** | -5.8 | 6e-07 | 28/38 (H4, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.791×** | -5.4 | 5e-06 | 26/48 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.793×** | -5.1 | 2e-05 | 27/47 (LOX-IMVI, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.804×** | -5.0 | 3e-05 | 25/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.805×** | -5.0 | 3e-05 | 24/48 (A-172, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.801×** | -4.9 | 4e-05 | 27/50 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.815×** | -4.7 | 1e-04 | 23/48 (HS-578T, HT-29, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -4.7 | 1e-04 | 24/48 (SNU-1, SK-MEL-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.822×** | -4.5 | 2e-04 | 23/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.704×** | -4.2 | 8e-04 | 22/47 (H4, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Allantoin (drug)]] 5 µM |  | 0.880× | -4.1 | 0.001 | 10/48 (LS 180, PANC-1, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | 0.848× | -3.8 | 0.004 | 22/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.892× | -3.7 | 0.006 | 13/48 (AsPC-1, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.862× | -3.4 | 0.014 | 19/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.858× | -3.4 | 0.015 | 13/48 (SW1417, RPMI-7951, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.866× | -3.3 | 0.018 | 13/48 (HOP62, NCI-H1792, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 0.861× | -3.3 | 0.018 | 21/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.865× | -3.2 | 0.025 | 17/49 (NCI-H1573, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 230 | 2 | 7 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.93× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 135 | 3 (1 ⚠) | 6 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.20× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Dexamethasone (drug)]] 5 µM 0.463× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 166 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 5 µM 0.439× (z -9.1) |
| [[SW1417 (line)]] | alt | 148 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.89× (z +16.2) | — |
| [[HOP62 (line)]] | alt | 191 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 122 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H1792 (line)]] | alt | 221 | 2 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.32× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -18.6) |
| [[NCI-H2030 (line)]] | alt | 129 | 2 | 2 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.63× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -12.2) |
| [[HS-578T (line)]] | alt | 165 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -16.8) |
| [[Panc 03.27 (line)]] | alt | 152 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[RPMI-7951 (line)]] | alt | 170 | 1 | 2 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.29× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 165 | 1 | 2 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.22× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -8.8) |
| [[A-427 (line)]] | wt | 84.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.08× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.384× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[A498 (line)]] | wt | 136 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[AsPC-1 (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 81.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[CFPAC-1 (line)]] | alt | 117 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -10.0) |
| [[H4 (line)]] | wt | 135 | 2 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.16× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -9.9) |
| [[PANC-1 (line)]] | alt | 71.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.1) | — |
| [[SW480 (line)]] | alt | 92.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 84.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.394× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[COLO 205 (line)]] | alt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HEC-1-A (line)]] | alt | 45.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 274 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.6) |
| [[KATO III (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[LoVo (line)]] | wt | 99.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 84.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.1) | — |
| [[RKO (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 162 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -11.8) |
| [[SW 1088 (line)]] | alt | 212 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0600× (z -13.3) |
| [[SW 900 (line)]] | alt | 136 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -12.2) |
| [[A549 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 113 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 169 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDLIM7]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[RAP1B]] | +0.67 | +0.57 / +0.68 | both halves | 8e-06 |  |
| [[TMEM184B]] | +0.66 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[GDI1]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[PLIN3]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[METRNL]] | +0.65 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[PORCN]] | +0.65 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[RTN2]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[DDAH2]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ARVCF]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.63 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[CLIP2]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHDC1]] | -0.61 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[COPS8-DT]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[RBBP4]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NAF1]] | -0.57 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MBNL3]] | -0.56 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ITPKB]] | -0.56 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[METAP1D]] | -0.56 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[RPRD1B]] | -0.56 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[PANK1]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CIAO2A]] | -0.55 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[DERA]] | -0.55 | -0.50 / -0.42 | both halves | 4e-05 | STRING 421 |
| [[ANAPC1]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT7]] | B | SYT7 activity lowers DLGAP4's level | lines that do not express SYT7 (9) vs lines expressing it (41) | 1.18× higher at baseline in the lines without SYT7 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CAVIN1]] | B | CAVIN1 activity raises DLGAP4's level | lines that do not express CAVIN1 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without CAVIN1 | 0.075 | ⚠ within organs, on part of the lines; also absent: NUAK1, SLC25A43, BLVRA |
| [[GFPT2]] | B | GFPT2 activity raises DLGAP4's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.38× lower at baseline in the lines without GFPT2 | 0.096 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.865). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.0, -1.9); signed map (-20.1, 25.1). **Vector** length 136, 43.0% of its response variance represented; |z| ≥ 3 in 1,392 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.2 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.6 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +6.2 | +9.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.9 | +7.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.2 | +5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.2 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -13.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.6 | -5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.2 | -4.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | DLG associated protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,306,336-36,528,637 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DAP4, KIAA0964, SAPAP4 |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2H0](https://www.uniprot.org/uniprotkb/Q9Y2H0) (DLG-associated protein 4):

> May play a role in the molecular organization of synapses and neuronal cell signaling. Could be an adapter protein linking ion channel to the subsynaptic cytoskeleton. May induce enrichment of PSD-95/SAP90 at the plasma membrane.

**Summary**, from NCBI Gene [22839](https://www.ncbi.nlm.nih.gov/gene/22839):

> The product of this gene is a membrane-associated guanylate kinase found at the postsynaptic density in neuronal cells. It is a signaling molecule that can interact with potassium channels and receptors, as well as other signaling molecules. The protein encoded by this gene can interact with PSD-95 through its guanylate kinase domain and may be involved in clustering PSD-95 in the postsynaptic density region. The encoded protein is one of at least four similar proteins that have been found. …

**Accessions** — [HGNC:24476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24476) · Entrez [22839](https://www.ncbi.nlm.nih.gov/gene/22839) · UniProt [Q9Y2H0](https://www.uniprot.org/uniprotkb/Q9Y2H0) · Ensembl [ENSG00000080845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080845)

## Data

Gene col 1296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1296); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1296]; `tensor/DDL_lfc|DDL_z.npy` [1296]; `embed/gene_vectors.npy` [1296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1296 or target_col == 1296). Every well: [[DLGAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLGAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
