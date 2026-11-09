---
symbol: "CAPN5"
type: "gene"
col: 7356
ensembl_id: "ENSG00000149260"
name: "calpain 5"
location: "11q13.5"
module: 30
arm: "+"
pooled_cpm: 23.87
n_lines_expressing: 46
n_dd_up: 16
n_dd_down: 38
n_dd_up_clean: 15
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# CAPN5

*calpain 5* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.28× (z +16.3, q 0e+00, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.416× (z -12.0, q 2e-30, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PREPL]] (+0.66, fdr 7e-06), [[SLC22A18]] (+0.65, fdr 1e-05), [[DOK4]] (+0.64, fdr 1e-05); moves opposite to [[P2RY11]] (-0.64, fdr 1e-05), [[ZNF407]] (-0.59, fdr 3e-05), [[ZRANB3]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CREB3L1]] → it (grade B ⚠); 2 go from it, the strongest it → [[NUTM2B-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7356.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.28×** | +16.3 | 0e+00 | 41/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **3.09×** | +15.5 | 0e+00 | 41/44 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.06×** | +14.0 | 3e-42 | 34/44 (PANC-1, SW480, …) | all doses, flat | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.68×** | +13.6 | 1e-39 | 42/44 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.57×** | +13.0 | 2e-36 | 40/44 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.55×** | +12.9 | 6e-36 | 35/44 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.36×** | +11.8 | 2e-30 | 38/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +7.1 | 8e-11 | 32/44 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +6.9 | 4e-10 | 29/44 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.09×** | +5.3 | 7e-06 | 25/44 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +4.9 | 5e-05 | 22/44 (AsPC-1, HEC-1-A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.74×** | +4.0 | 0.003 | 12/43 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.011 | 13/44 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.023 | 16/44 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.18× | +3.2 | 0.049 | 4/44 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.050 | 11/44 (KATO III, A549, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.050 | 10/44 (KATO III, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7356.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.416×** | -12.0 | 2e-30 | 39/44 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.478×** | -10.1 | 1e-21 | 32/44 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.485×** | -9.9 | 8e-21 | 29/42 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.493×** | -9.7 | 5e-20 | 31/44 (COLO 205, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.500×** | -9.5 | 3e-19 | 28/36 (SW1417, NCI-H2347, …) | all doses, flat | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.556×** | -8.0 | 8e-14 | 33/44 (HT-29, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.580×** | -7.5 | 7e-12 | 23/41 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -7.3 | 2e-11 | 24/42 (NCI-H2347, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.614×** | -6.4 | 9e-09 | 27/40 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.610×** | -6.3 | 2e-08 | 21/31 (NCI-H2347, hTERT-HPNE, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.672×** | -5.4 | 3e-06 | 21/43 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -5.2 | 1e-05 | 22/44 (KATO III, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.685×** | -5.2 | 1e-05 | 20/44 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.705×** | -4.8 | 7e-05 | 17/43 (CFPAC-1, HT-29, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.700×** | -4.7 | 1e-04 | 19/28 (HT-29, Panc 03.27, …) | all doses, flat | composition shift; position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **0.625×** | -4.6 | 1e-04 | 19/44 (RPMI-7951, A-172, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.720×** | -4.3 | 5e-04 | 16/43 (H4, SW 1271, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.738×** | -4.1 | 0.001 | 18/44 (SW 1271, CHP-212, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.748×** | -4.0 | 0.002 | 15/44 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Acetohexamide (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.006 | 12/44 (COLO 205, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.006 | 15/44 (HT-29, A-172, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | **0.828×** | -3.6 | 0.006 | 15/44 (SNU-1, SW1417, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.768×** | -3.6 | 0.007 | 15/44 (C-33 A, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.770×** | -3.4 | 0.015 | 15/43 (LOX-IMVI, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 101 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.170× (z -14.3) |
| [[PANC-1 (line)]] | alt | 12.2 | 6 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 6.00× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[LoVo (line)]] | wt | 22.7 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.146× (z -11.2) |
| [[KATO III (line)]] | alt | 108 | 0 | 7 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.244× (z -12.0) |
| [[SW480 (line)]] | alt | 15.2 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 4.57× (z +10.4) | [[Digitoxin (drug)]] 0.05 µM 0.275× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 65.5 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -11.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 35.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0413× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 11.8 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.84× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.09 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 0.05 µM 8.31× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 77.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0612× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 47.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.331× (z -8.7) |
| [[Hs 766T (line)]] | wt | 21.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 7.43 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.63× (z +8.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 6.04× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 40.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0874× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -8.5) |
| [[A-427 (line)]] | wt | 16.0 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.74× (z +8.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A549 (line)]] | wt | 9.39 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.42× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 39.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.204× (z -9.8) |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0662× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 8.50 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 14.0× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0876× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PREPL]] | +0.66 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[SLC22A18]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[DOK4]] | +0.64 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MIR29B2CHG]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[UNC119]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PPDPF]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[ORC4]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ALAD]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[NGFR]] | +0.62 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[SLC44A2]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[GALM]] | +0.61 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[AHDC1]] | +0.60 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RY11]] | -0.64 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[ZNF407]] | -0.59 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[ZRANB3]] | -0.59 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[SPON1-AS1]] | -0.58 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[AVEN]] | -0.57 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[MIATNB]] | -0.56 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[AGAP6]] | -0.56 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ASXL2]] | -0.56 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[ST7L]] | -0.56 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[DNAJC11]] | -0.55 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[PRMT3]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[SLC39A10]] | -0.55 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB3L1]] | B | CREB3L1 activity raises CAPN5's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.77× lower at baseline in the lines without CREB3L1 | 0.062 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUTM2B-AS1]] | C | CAPN5 activity lowers NUTM2B-AS1's level | lines that do not express CAPN5 (4) vs lines expressing it (46) | 2.16× higher at baseline in the lines without CAPN5 | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22, PLEKHF1; maybe low, not absent |
| [[CAT]] | C | CAPN5 activity raises CAT's level | lines that do not express CAPN5 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without CAPN5 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22, PLEKHF1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (2.8, -8.0); signed map (-25.5, -6.0). **Vector** length 120, 33.7% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +11.5 | +14.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +8.7 | +12.9 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +6.9 | +15.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +13.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.3 | +11.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +0.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.5 | +2.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.3 | -12.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.0 | -10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -8.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.2 | -5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | calpain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:77,066,961-77,126,155 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nCL-3, HTRA3, ADNIV; previously VRNI |
| Gene groups (HGNC) | C2 domain containing; Calpains |
| Hallmark sets | COAGULATION, GLYCOLYSIS |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O15484](https://www.uniprot.org/uniprotkb/O15484) (Calpain-5):

> Calcium-regulated non-lysosomal thiol-protease.

**Summary**, from NCBI Gene [726](https://www.ncbi.nlm.nih.gov/gene/726):

> Calpains are calcium-dependent cysteine proteases involved in signal transduction in a variety of cellular processes. A functional calpain protein consists of an invariant small subunit and 1 of a family of large subunits. CAPN5 is one of the large subunits. Unlike some of the calpains, CAPN5 and CAPN6 lack a calmodulin-like domain IV. Because of the significant similarity to Caenorhabditis elegans sex determination gene tra-3, CAPN5 is also called as HTRA3. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1482) · Entrez [726](https://www.ncbi.nlm.nih.gov/gene/726) · UniProt [O15484](https://www.uniprot.org/uniprotkb/O15484) · Ensembl [ENSG00000149260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149260)

## Data

Gene col 7356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7356); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7356]; `tensor/DDL_lfc|DDL_z.npy` [7356]; `embed/gene_vectors.npy` [7356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7356 or target_col == 7356). Every well: [[CAPN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
