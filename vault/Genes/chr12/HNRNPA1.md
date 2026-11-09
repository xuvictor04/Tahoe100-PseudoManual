---
symbol: "HNRNPA1"
type: "gene"
col: 5715
ensembl_id: "ENSG00000135486"
name: "heterogeneous nuclear ribonucleoprotein A1"
location: "12q13.13"
module: 43
arm: "+"
pooled_cpm: 312.41
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# HNRNPA1

*heterogeneous nuclear ribonucleoprotein A1* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.57× (z +17.9, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.68× (z +3.8, q 0.012, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.744× (z -5.8, q 4e-06, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL3]] (+0.79, fdr 7e-06), [[NPM1]] (+0.74, fdr 7e-06), [[HNRNPA1L3]] (+0.72, fdr 7e-06); moves opposite to [[RBX1]] (-0.62, fdr 1e-05), [[C14orf119]] (-0.61, fdr 3e-05), [[ZCCHC10]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRTAP]] → it (grade C ⚠); 1 goes from it, the strongest it → [[NPM1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +17.9 | 0e+00 | 49/49 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +14.7 | 0e+00 | 44/44 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +12.1 | 2e-31 | 45/45 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.8 | 2e-09 | 41/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.43×** | +5.0 | 5e-05 | 46/48 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.012 | 36/48 (LoVo, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.035 | 32/48 (LoVo, HepG2/C3A, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.059 | 29/48 (NCI-H1792, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.744×** | -5.8 | 4e-06 | 30/48 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.667×** | -5.7 | 4e-06 | 44/48 (HepG2/C3A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.805×** | -4.2 | 0.004 | 31/48 (NCI-H23, A-427, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.824×** | -3.8 | 0.024 | 26/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.776×** | -3.5 | 0.045 | 40/49 (HT-29, NCI-H23, …) | inconsistent across doses |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.099 | 28/47 (RKO, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Olanzapine (drug)]] 5 µM |  | 0.849× | -3.2 | 0.11 | 11/48 (RKO, SW 900, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.797× | -3.2 | 0.11 | 26/49 (SW1417, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 514 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +14.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -16.1) |
| [[KATO III (line)]] | alt | 255 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +19.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 245 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +17.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 394 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -14.1) |
| [[SW48 (line)]] | wt | 459 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +14.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -9.7) |
| [[A-427 (line)]] | wt | 361 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -10.2) |
| [[C-33 A (line)]] | alt | 408 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.6) |
| [[C32 (line)]] | wt | 193 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 280 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +16.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 529 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +17.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 381 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 369 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.39× (z +10.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -14.0) ⚠ cell-cycle shift, explains ~9% of this change |
| [[A-172 (line)]] | wt | 137 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +13.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 205 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 355 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +16.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 330 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 284 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +13.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 252 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +15.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 207 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 298 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +17.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 229 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +15.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 438 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 190 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +14.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 366 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -17.4) |
| [[Panc 03.27 (line)]] | alt | 363 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +17.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 209 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +14.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 437 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +14.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 172 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 244 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +15.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.9) |
| [[SNU-1 (line)]] | wt | 480 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -25.0) |
| [[SNU-423 (line)]] | alt | 279 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 202 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +16.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 633 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 230 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +14.8) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 325 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +9.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 203 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +15.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 291 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 382 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +13.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 201 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +10.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 269 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +11.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 443 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 406 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +11.1) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 231 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +13.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 272 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +14.0) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 200 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.0402× (z -15.4) |
| [[BT-474 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 359 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 222 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL3]] | +0.79 | +0.72 / +0.79 | both halves | 7e-06 | STRING 514 |
| [[NPM1]] | +0.74 | +0.62 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 923 |
| [[HNRNPA1L3]] | +0.72 | +0.78 / +0.72 | both halves | 7e-06 | STRING 801 |
| [[RPL4]] | +0.71 | +0.69 / +0.76 | both halves | 7e-06 | STRING 623 |
| [[PCBP2]] | +0.69 | +0.64 / +0.75 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 940 |
| [[RPL14]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[NONO]] | +0.67 | +0.71 / +0.65 | both halves | 7e-06 | same gene group; STRING 945 |
| [[RPS3A]] | +0.66 | +0.71 / +0.69 | both halves | 7e-06 | pathway: SARS-CoV-1 Infection; STRING 693 |
| [[EEF2]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 | STRING 777 |
| [[CRTAP]] | +0.63 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.63 | +0.71 / +0.72 | both halves | 7e-06 | pathway: SARS-CoV-1 Infection; STRING 662 |
| [[SSRP1]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBX1]] | -0.62 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[C14orf119]] | -0.61 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[ZCCHC10]] | -0.60 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MED18]] | -0.59 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ERVK3-1]] | -0.58 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.55 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[PPP1R14B-AS1]] | -0.55 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[NDUFA13]] ⚠ | -0.54 | -0.49 / -0.52 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZCCHC3]] | -0.53 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[GORASP1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ZNF503]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[DOHH]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[MAD2L1BP]] | -0.52 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRTAP]] | C | CRTAP activity raises HNRNPA1's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.37× lower at baseline in the lines without CRTAP | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPM1]] | C | HNRNPA1's natural level weakens NPM1's drug response | HNRNPA1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.01; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.278). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-30.1, -25.5); signed map (-22.4, -33.6). **Vector** length 121, 45.4% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +12.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.3 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.9 | +1.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -9.5 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.1 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.4 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.0 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:54,280,193-54,287,088 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hnRNP-A1, ALS20; previously HNRPA1 |
| Gene groups (HGNC) | RNA binding motif containing; Spliceosomal A complex; Heterogeneous nuclear ribonucleoproteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 17 pathways, smallest: FGFR2 alternative splicing; SARS-CoV-1 modulates host translation machinery; Signaling by FGFR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P09651](https://www.uniprot.org/uniprotkb/P09651) (Heterogeneous nuclear ribonucleoprotein A1):

> Involved in the packaging of pre-mRNA into hnRNP particles, transport of poly(A) mRNA from the nucleus to the cytoplasm and modulation of splice site selection. Plays a role in the splicing of pyruvate kinase PKM by binding repressively to sequences flanking PKM exon 9, inhibiting exon 9 inclusion and resulting in exon 10 inclusion and production of the PKM M2 isoform. Binds to the IRES and thereby inhibits the translation of the apoptosis protease activating factor APAF1. May bind to specific …

**Summary**, from NCBI Gene [3178](https://www.ncbi.nlm.nih.gov/gene/3178):

> This gene encodes a member of a family of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs), which are RNA-binding proteins that associate with pre-mRNAs in the nucleus and influence pre-mRNA processing, as well as other aspects of mRNA metabolism and transport. The protein encoded by this gene is one of the most abundant core proteins of hnRNP complexes and plays a key role in the regulation of alternative splicing. Mutations in this gene have been observed in …

**Accessions** — [HGNC:5031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5031) · Entrez [3178](https://www.ncbi.nlm.nih.gov/gene/3178) · UniProt [P09651](https://www.uniprot.org/uniprotkb/P09651) · Ensembl [ENSG00000135486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135486)

## Data

Gene col 5715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5715); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5715]; `tensor/DDL_lfc|DDL_z.npy` [5715]; `embed/gene_vectors.npy` [5715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5715 or target_col == 5715). Every well: [[HNRNPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
