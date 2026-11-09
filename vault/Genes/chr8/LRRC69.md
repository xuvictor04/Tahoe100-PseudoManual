---
symbol: "LRRC69"
type: "gene"
col: 13234
ensembl_id: "ENSG00000214954"
name: "leucine rich repeat containing 69"
location: "8q21.3"
module: 5
arm: "+"
pooled_cpm: 27.9
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# LRRC69

*leucine rich repeat containing 69* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.29× (z +11.3, q 6e-27, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.74× (z +7.6, q 3e-12, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.441× (z -6.3, q 2e-07, down in 37 of 45 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Dimethyl fumarate (drug)]] 5 µM: 0.771× (z -3.7, q 0.064, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C-33 A 0.0993×, NCI-H23 0.244×, PANC-1 0.364×, J82 0.236×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HepG2/C3A 0.343×, NCI-H23 0.429×, NCI-H2030 0.457×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.258×, RKO 0.339×; ⚠ cell-cycle shift, would explain all of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2030 0.246×); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.196×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2F-SCLY]] (+0.65, fdr 7e-06), [[PRDM15]] (+0.64, fdr 1e-05), [[KANSL1L-AS1]] (+0.62, fdr 1e-05); moves opposite to [[RING1]] (-0.59, fdr 2e-05), [[ZNF184]] (-0.56, fdr 1e-04), [[SUPT20H]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SCLY]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.29×** | +11.3 | 6e-27 | 39/48 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.14×** | +10.7 | 3e-24 | 41/47 (SW480, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +10.7 | 3e-24 | 38/48 (SHP-77, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.98×** | +9.3 | 1e-18 | 38/47 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.90×** | +9.0 | 4e-17 | 39/48 (SW480, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.82×** | +8.7 | 3e-16 | 34/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.76×** | +7.7 | 1e-12 | 36/47 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +7.6 | 3e-12 | 30/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +7.0 | 1e-10 | 34/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.64×** | +6.9 | 2e-10 | 30/47 (SW 900, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.8 | 4e-10 | 33/48 (SW1417, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.5 | 3e-09 | 26/47 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +6.5 | 4e-09 | 34/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +6.4 | 6e-09 | 32/47 (HOP62, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.50×** | +5.9 | 1e-07 | 28/47 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +5.8 | 3e-07 | 28/47 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +5.6 | 8e-07 | 27/47 (SHP-77, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +4.7 | 6e-05 | 23/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[EX229 (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.005 | 16/47 (LoVo, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.009 | 13/47 (LOX-IMVI, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.011 | 12/47 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.017 | 12/47 (AsPC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Gefitinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.023 | 9/48 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.026 | 13/47 (A498, LoVo, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.040 | 9/48 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | 1.16× | +3.1 | 0.040 | 10/48 (MIA PaCa-2, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13234.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C-33 A 0.0993×, NCI-H23 0.244×, PANC-1 0.364×, J82 0.236×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HepG2/C3A 0.343×, NCI-H23 0.429×, NCI-H2030 0.457×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.258×, RKO 0.339×; ⚠ cell-cycle shift, would explain all of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2030 0.246×); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.196×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.441×** | -6.3 | 2e-07 | 37/45 (RKO, C32, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.771×** | -3.7 | 0.064 | 15/47 (PANC-1, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.786×** | -3.5 | 0.073 | 18/46 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.791× | -3.3 | 0.11 | 11/48 (NCI-H1792, SW 900, …) | top dose only | plate-row cell shift |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.791× | -3.3 | 0.11 | 11/46 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.792× | -3.2 | 0.11 | 10/48 (NCI-H1573, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 31.0 | 0 | 4 (3 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.246× (z -10.2) |
| [[LoVo (line)]] | wt | 19.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +10.0) | — |
| [[RKO (line)]] | wt | 92.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | [[Harringtonine (drug)]] 5 µM 0.339× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 33.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +11.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 37.7 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.196× (z -9.9) |
| [[HS-578T (line)]] | alt | 40.8 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 20.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.74× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 41.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 18.8 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 21.3 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +13.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[C-33 A (line)]] | alt | 62.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0993× (z -17.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[NCI-H1792 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 23.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.57× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[PANC-1 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -10.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.18× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW1417 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2F-SCLY]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PRDM15]] | +0.64 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[KANSL1L-AS1]] | +0.62 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[DCAF4L1]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[NUTM2A-AS1]] | +0.62 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[NUTM2B-AS1]] | +0.61 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[FRZB]] | +0.60 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[MFSD14CP-1]] | +0.60 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[LARS2]] | +0.59 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[RAPSN]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PSMD6-AS2]] | +0.58 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[LYRM4]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RING1]] | -0.59 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ZNF184]] | -0.56 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[SUPT20H]] | -0.53 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[MMUT]] | -0.52 | -0.60 / -0.37 | both halves | 9e-05 |  |
| [[SNAPIN]] | -0.51 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[FAM161B]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CD99P1]] | -0.50 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ILK]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[DBP]] | -0.50 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[AAAS]] | -0.49 | -0.52 / -0.21 | both halves | 6e-04 |  |
| [[PADI2]] | -0.49 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[ACTR1B]] | -0.49 | -0.51 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRRC69's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC26A7]] | C | SLC26A7 activity raises LRRC69's level | lines that do not express SLC26A7 (4) vs lines expressing it (46) | 2.51× lower at baseline in the lines without SLC26A7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[SCOC]] | C | SCOC activity lowers LRRC69's level | lines that do not express SCOC (4) vs lines expressing it (46) | 1.65× higher at baseline in the lines without SCOC | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCLY]] | C | LRRC69's natural level weakens SCLY's drug response | LRRC69's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.29; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (20.6, -13.9); signed map (9.9, -6.5). **Vector** length 105, 27.1% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.1 | +5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.9 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.1 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.0 | +7.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +6.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.9 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +6.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.4 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.6 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | -4.0 | -3.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -3.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 69 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:91,101,832-91,219,257 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q6ZNQ3](https://www.uniprot.org/uniprotkb/Q6ZNQ3) carries no function annotation.

**Summary**, from NCBI Gene [100130742](https://www.ncbi.nlm.nih.gov/gene/100130742):

> Predicted to be involved in intracellular signal transduction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34303) · Entrez [100130742](https://www.ncbi.nlm.nih.gov/gene/100130742) · UniProt [Q6ZNQ3](https://www.uniprot.org/uniprotkb/Q6ZNQ3) · Ensembl [ENSG00000214954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214954)

## Data

Gene col 13234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13234); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13234]; `tensor/DDL_lfc|DDL_z.npy` [13234]; `embed/gene_vectors.npy` [13234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13234 or target_col == 13234). Every well: [[LRRC69 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC69.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
