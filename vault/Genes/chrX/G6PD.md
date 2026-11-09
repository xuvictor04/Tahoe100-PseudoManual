---
symbol: "G6PD"
type: "gene"
col: 8320
ensembl_id: "ENSG00000160211"
name: "glucose-6-phosphate dehydrogenase"
location: "Xq28"
module: 20
arm: "+"
pooled_cpm: 35.11
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# G6PD

*glucose-6-phosphate dehydrogenase* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.69× (z +20.5, q 0e+00, up in 42 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.98× (z +9.1, q 1e-17, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.664× (z -5.4, q 3e-05, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.726× (z -4.3, q 0.004, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2E]] (+0.63, fdr 1e-05), [[ASPH]] (+0.60, fdr 1e-05), [[HAPSTR1]] (+0.60, fdr 1e-05); moves opposite to [[MRPL32]] (-0.66, fdr 1e-05), [[RWDD3]] (-0.61, fdr 1e-05), [[SRSF11]] (-0.61, fdr 1e-05, ⚠ SRSF11 in the vector space only through flagged drug-doses), [[MRPS18C]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8320.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.69×** | +20.5 | 0e+00 | 42/42 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.06×** | +17.9 | 0e+00 | 36/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.50×** | +15.4 | 0e+00 | 37/38 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.28×** | +11.0 | 9e-26 | 44/48 (KATO III, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.42×** | +10.1 | 4e-22 | 45/48 (KATO III, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.03×** | +9.4 | 4e-19 | 40/48 (KATO III, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +9.1 | 1e-17 | 39/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +6.6 | 2e-09 | 34/48 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.40×** | +6.3 | 2e-08 | 27/46 (SNU-423, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 1e-05 | 33/47 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.44×** | +4.7 | 2e-04 | 27/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.41×** | +4.5 | 3e-04 | 25/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.001 | 23/48 (CFPAC-1, HOP62, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.37×** | +4.0 | 0.003 | 22/45 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.32×** | +3.7 | 0.007 | 18/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.066 | 12/47 (H4, PANC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.069 | 12/48 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.078 | 15/48 (NCI-H1792, NCI-H1573, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.54×** | +3.0 | 0.079 | 14/46 (A498, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.083 | 13/46 (HCT15, SW 900, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.099 | 9/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8320.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.664×** | -5.4 | 3e-05 | 25/48 (SNU-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.726×** | -4.3 | 0.004 | 23/48 (BT-474, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.798×** | -4.2 | 0.004 | 23/48 (H4, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **0.816×** | -3.8 | 0.017 | 20/48 (SNU-423, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bergenin (drug)]] 5 µM |  | **0.829×** | -3.5 | 0.044 | 14/48 (HT-29, SNU-1, …) | top dose only | position effect removed |
| [[Ciclopirox (drug)]] 5 µM |  | 0.834× | -3.4 | 0.057 | 20/48 (H4, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.787× | -3.2 | 0.11 | 17/48 (BT-474, SHP-77, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.2 | 0.11 | 25/47 (HT-29, BT-474, …) | top dose only | composition shift |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.782× | -3.1 | 0.12 | 15/48 (J82, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Trimetrexate (drug)]] 5 µM |  | 0.850× | -3.1 | 0.12 | 16/48 (HOP62, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 33.4 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.63× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 69.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.0× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 44.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.85× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 12.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.38× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.1× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 22.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.40× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A498 (line)]] | wt | 51.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 42.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.34× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 30.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[J82 (line)]] | alt | 65.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 52.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 24.9× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 43.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 79.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.33× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 50.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 27.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 12.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.79× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0846× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 21.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[Hs 766T (line)]] | wt | 50.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HT-29 (line)]] | alt | 61.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.90× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 33.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.70× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LOX-IMVI (line)]] | wt | 25.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 16.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.86× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 42.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.103× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~78% of this change |
| [[AsPC-1 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.08× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0943× (z -16.5) ⚠ toxic; cell-cycle shift, explains ~56% of this change |
| [[NCI-H2347 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SHP-77 (line)]] | alt | 47.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 23.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2E]] | +0.63 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ASPH]] | +0.60 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HAPSTR1]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PKM]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 941 |
| [[PGD]] | +0.60 | +0.56 / +0.63 | both halves | 1e-05 | same gene group; pathway: Cellular response to chemical stress; STRING 999 |
| [[AP2M1]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[DPM2]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[NORAD]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ACLY]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 785 |
| [[YWHAQ]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 | pathway: TP53 Regulates Metabolic Genes |
| [[MAPRE1]] | +0.58 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL32]] | -0.66 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[RWDD3]] | -0.61 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[SRSF11]] ⚠ | -0.61 | -0.56 / -0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18C]] | -0.61 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[CROCCP2-1]] | -0.61 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[ZNF330]] | -0.60 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[TERF2IP]] | -0.60 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ADPRM]] | -0.60 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[PPIG]] | -0.59 | -0.47 / -0.55 | both halves | 2e-05 | STRING 590 |
| [[SETDB1]] | -0.58 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.58 | -0.53 / -0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF1B]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TATDN3]] | -0.57 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[NDUFC1]] | -0.57 | -0.43 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers G6PD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.2, 22.8); signed map (-12.2, 33.3). **Vector** length 103, 27.7% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.2 | +20.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +15.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +2.8 | +17.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +2.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +2.5 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -6.5 | -4.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.1 | -5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.2 | -2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -3.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.9 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.7 | -1.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.4 | -1.7 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | -2.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | glucose-6-phosphate dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,517,825-154,547,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G6PD1 |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, GLYCOLYSIS, MTORC1_SIGNALING |
| Reactome | 10 pathways, smallest: NFE2L2 regulates pentose phosphate pathway genes; Pentose phosphate pathway; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P11413](https://www.uniprot.org/uniprotkb/P11413) (Glucose-6-phosphate 1-dehydrogenase):

> Catalyzes the rate-limiting step of the oxidative pentose-phosphate pathway, which represents a route for the dissimilation of carbohydrates besides glycolysis. The main function of this enzyme is to provide reducing power (NADPH) and pentose phosphates for fatty acid and nucleic acid synthesis. Also catalyzes the conversion of NAADPH, which is produced by enzymes such as DUOX1, DUOX2 and NOX5 from NAADP and promotes Ca(2+) signaling during T cell activation, back to NAADP.

**Summary**, from NCBI Gene [2539](https://www.ncbi.nlm.nih.gov/gene/2539):

> This gene encodes glucose-6-phosphate dehydrogenase. This protein is a cytosolic enzyme encoded by a housekeeping X-linked gene whose main function is to produce NADPH, a key electron donor in the defense against oxidizing agents and in reductive biosynthetic reactions. G6PD is remarkable for its genetic diversity. Many variants of G6PD, mostly produced from missense mutations, have been described with wide ranging levels of enzyme activity and associated clinical symptoms. G6PD deficiency may …

**Accessions** — [HGNC:4057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4057) · Entrez [2539](https://www.ncbi.nlm.nih.gov/gene/2539) · UniProt [P11413](https://www.uniprot.org/uniprotkb/P11413) · Ensembl [ENSG00000160211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160211)

## Data

Gene col 8320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8320); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8320]; `tensor/DDL_lfc|DDL_z.npy` [8320]; `embed/gene_vectors.npy` [8320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8320 or target_col == 8320). Every well: [[G6PD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/G6PD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
