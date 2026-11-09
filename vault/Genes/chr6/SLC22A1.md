---
symbol: "SLC22A1"
type: "gene"
col: 10551
ensembl_id: "ENSG00000175003"
name: "solute carrier family 22 member 1"
location: "6q25.3"
module: 39
arm: "+"
pooled_cpm: 8.16
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# SLC22A1

*solute carrier family 22 member 1* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.37× (z +23.2, q 0e+00, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.363× (z -7.8, q 3e-12, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C3orf20]] (+0.86, fdr 7e-06), [[GARIN1A]] (+0.83, fdr 7e-06), [[USP50]] (+0.83, fdr 7e-06); moves opposite to [[RPA1]] (-0.70, fdr 7e-06), [[SLC9A6]] (-0.65, fdr 1e-05), [[PMS2P3-1]] (-0.64, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.37×** | +23.2 | 0e+00 | 41/44 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.18×** | +14.1 | 2e-42 | 40/41 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **6.43×** | +13.8 | 3e-41 | 37/45 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +11.7 | 3e-29 | 38/40 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.97×** | +8.4 | 4e-15 | 37/46 (A-172, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +6.1 | 9e-08 | 35/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +5.6 | 2e-06 | 23/42 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.5 | 2e-06 | 23/48 (A-172, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +5.5 | 2e-06 | 26/47 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.01×** | +5.4 | 4e-06 | 25/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +5.3 | 6e-06 | 10/24 (HOP62, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.66×** | +3.9 | 0.004 | 19/47 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.42×** | +3.8 | 0.006 | 20/47 (A498, SNU-1, …) | all doses, flat | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.011 | 15/47 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.033 | 15/42 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.056 | 16/47 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.088 | 16/48 (SW480, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.363×** | -7.8 | 3e-12 | 31/47 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.435×** | -6.4 | 4e-08 | 29/46 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.455×** | -6.1 | 2e-07 | 26/42 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.502×** | -5.3 | 1e-05 | 26/46 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.493×** | -5.2 | 2e-05 | 22/36 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.550×** | -4.4 | 9e-04 | 21/37 (SNU-423, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.576×** | -4.0 | 0.005 | 16/44 (MIA PaCa-2, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.612×** | -3.6 | 0.019 | 16/45 (SW 900, HEC-1-A, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.730×** | -3.4 | 0.038 | 12/48 (COLO 205, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -3.4 | 0.043 | 17/48 (KATO III, NCI-H1573, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.466× | -3.1 | 0.11 | 10/37 (HepG2/C3A, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.667× | -3.0 | 0.13 | 15/44 (HS-578T, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.8 | 2 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0836× (z -13.9) |
| [[SNU-423 (line)]] | alt | 19.0 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +12.3) | [[Belinostat (drug)]] 0.5 µM 0.0412× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.114× (z -9.5) |
| [[A549 (line)]] | wt | 4.25 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.6× (z +14.1) | — |
| [[HepG2_C3A (line)]] | wt | 25.0 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 8.34 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +15.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0639× (z -10.4) |
| [[PANC-1 (line)]] | alt | 5.30 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +13.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0993× (z -9.8) |
| [[SW 900 (line)]] | alt | 11.5 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +11.9) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0674× (z -9.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.0794× (z -8.9) |
| [[A-172 (line)]] | wt | 7.56 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 3.21 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 88.8× (z +15.0) | — |
| [[HT-29 (line)]] | alt | 9.06 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.0561× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.106× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 5.76 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 42.4× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 2.57 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.3× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 6.26 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +17.0) | — |
| [[Panc 03.27 (line)]] | alt | 4.18 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.4× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 3.69 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.15× (z +8.7) | [[Belumosudil (drug)]] 0.5 µM 0.0431× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 3.10 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 25.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +11.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0759× (z -11.0) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 17.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0990× (z -12.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 9.62 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.0437× (z -11.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 10.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +15.8) | — |
| [[KATO III (line)]] | alt | 9.13 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0640× (z -9.8) |
| [[LoVo (line)]] | wt | 7.26 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 5.43 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.57× (z +9.5) | [[Digitoxin (drug)]] 0.5 µM 0.0654× (z -9.1) |
| [[RKO (line)]] | wt | 9.30 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 47.5× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 25.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -9.1) |
| [[SW48 (line)]] | wt | 7.25 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +10.9) | — |
| [[A-427 (line)]] | wt | 6.00 | 0 | 1 | — | [[Captopril (drug)]] 0.5 µM 0.0687× (z -9.5) |
| [[BT-474 (line)]] | alt | 6.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +12.0) | — |
| [[C32 (line)]] | wt | 4.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 2.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.7× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0754× (z -11.2) |
| [[SW1417 (line)]] | alt | 6.98 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0608× (z -9.9) |
| [[A498 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf20]] | +0.86 | +0.90 / +0.76 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.83 | +0.85 / +0.71 | both halves | 7e-06 |  |
| [[USP50]] | +0.83 | +0.87 / +0.74 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.82 | +0.83 / +0.77 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.82 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.81 | +0.82 / +0.74 | both halves | 7e-06 | pathway: Neuronal System |
| [[MYOCOS]] | +0.81 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.80 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.80 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[LINC02803]] | +0.80 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.79 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.78 | +0.85 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | -0.70 | -0.77 / -0.62 | both halves | 7e-06 |  |
| [[SLC9A6]] | -0.65 | -0.73 / -0.54 | both halves | 1e-05 | pathway: SLC-mediated transmembrane transport |
| [[PMS2P3-1]] | -0.64 | -0.73 / -0.59 | both halves | 7e-06 |  |
| [[PXMP4]] | -0.64 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[BRAT1]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC22A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01252]] | B | LINC01252 activity raises SLC22A1's level | lines that do not express LINC01252 (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without LINC01252 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000275119, EPHB6, ABCC2; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises SLC22A1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without FSIP2-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC01917]] | B | LINC01917 activity raises SLC22A1's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.32× lower at baseline in the lines without LINC01917 | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[MMP25]] | C | MMP25 activity raises SLC22A1's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.859). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.2, -13.0); signed map (18.4, 8.3). **Vector** length 106, 26.0% of its response variance represented; |z| ≥ 3 in 1,449 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.6 | +14.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.4 | +23.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +13.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +5.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.7 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +5.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.3 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.2 | -5.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -4.1 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | +0.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 22 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:160,121,815-160,158,718 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OCT1 |
| Gene groups (HGNC) | Solute carrier family 22 |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 13 pathways, smallest: Ciprofloxacin ADME; Abacavir transmembrane transport; Neurotransmitter clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [O15245](https://www.uniprot.org/uniprotkb/O15245) (Solute carrier family 22 member 1):

> Electrogenic voltage-dependent uniporter that mediates the transport of a variety of organic cations such as endogenous bioactive amines, cationic drugs and xenobiotics. Functions as a pH- and Na(+)-independent, bidirectional transporter (By similarity). Cation cellular uptake or release is driven by the electrochemical potential (i.e. membrane potential and concentration gradient) and substrate selectivity (By similarity). Hydrophobicity is a major requirement for recognition in polyvalent …

**Summary**, from NCBI Gene [6580](https://www.ncbi.nlm.nih.gov/gene/6580):

> Polyspecific organic cation transporters in the liver, kidney, intestine, and other organs are critical for elimination of many endogenous small organic cations as well as a wide array of drugs and environmental toxins. This gene is one of three similar cation transporter genes located in a cluster on chromosome 6. The encoded protein contains twelve putative transmembrane domains and is a plasma integral membrane protein. Two transcript variants encoding two different isoforms have been found …

**Accessions** — [HGNC:10963](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10963) · Entrez [6580](https://www.ncbi.nlm.nih.gov/gene/6580) · UniProt [O15245](https://www.uniprot.org/uniprotkb/O15245) · Ensembl [ENSG00000175003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175003)

## Data

Gene col 10551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10551); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10551]; `tensor/DDL_lfc|DDL_z.npy` [10551]; `embed/gene_vectors.npy` [10551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10551 or target_col == 10551). Every well: [[SLC22A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC22A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
