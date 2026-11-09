---
symbol: "SLC16A1"
type: "gene"
col: 7893
ensembl_id: "ENSG00000155380"
name: "solute carrier family 16 member 1"
location: "1p13.2"
module: 93
arm: "+"
pooled_cpm: 100.84
n_lines_expressing: 47
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# SLC16A1

*solute carrier family 16 member 1* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +15.8, q 0e+00, up in 32 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.389×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 0.300×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.354×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFRC]] (+0.63, fdr 7e-06), [[BZW2]] (+0.61, fdr 1e-05), [[AMD1]] (+0.61, fdr 1e-05); moves opposite to [[ZSCAN16]] (-0.47, fdr 8e-05), [[SMIM7]] (-0.46, fdr 5e-05), [[PPP6C]] (-0.45, fdr 4e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AFAP1-AS1]] → it (grade B ⚠); 3 go from it, the strongest it → [[PYGM]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +15.8 | 0e+00 | 32/45 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +14.6 | 0e+00 | 40/46 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.83×** | +9.1 | 3e-17 | 39/45 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.59×** | +7.0 | 5e-10 | 34/45 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.59×** | +6.9 | 5e-10 | 28/45 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +6.5 | 6e-09 | 37/45 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.51×** | +6.2 | 6e-08 | 29/45 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +6.1 | 7e-08 | 25/45 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.8 | 5e-07 | 34/45 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.56×** | +5.4 | 5e-06 | 28/45 (Panc 03.27, hTERT-HPNE, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.8 | 7e-05 | 29/45 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +4.7 | 1e-04 | 25/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.43×** | +4.7 | 1e-04 | 28/45 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.40×** | +4.5 | 3e-04 | 26/45 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.34×** | +4.4 | 4e-04 | 26/45 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +3.8 | 0.004 | 23/45 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.017 | 17/45 (NCI-H23, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.017 | 21/45 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.021 | 23/45 (Hs 766T, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.022 | 19/45 (Hs 766T, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.022 | 19/45 (SHP-77, RKO, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.022 | 19/45 (Hs 766T, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.023 | 20/45 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.046 | 16/46 (A498, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7893.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.389×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 0.300×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.354×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | 0.799× | -3.3 | 0.27 | 19/45 (LoVo, LS 180, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.797× | -3.3 | 0.27 | 20/46 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.865× | -3.0 | 0.40 | 15/45 (LoVo, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 56.0 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +19.0) | — |
| [[NCI-H460 (line)]] | wt | 77.1 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 81.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +17.9) | — |
| [[CFPAC-1 (line)]] | alt | 37.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +19.6) | — |
| [[HOP62 (line)]] | alt | 66.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +17.6) | — |
| [[Hs 766T (line)]] | wt | 67.1 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +14.4) | — |
| [[hTERT-HPNE (line)]] | wt | 61.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +18.9) | — |
| [[NCI-H1792 (line)]] | alt | 86.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +18.6) | — |
| [[SK-MEL-2 (line)]] | alt | 213 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 57.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 153 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.7) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.354× (z -10.2) |
| [[HT-29 (line)]] | alt | 56.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +16.3) | — |
| [[J82 (line)]] | alt | 85.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 63.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +14.6) | — |
| [[RPMI-7951 (line)]] | alt | 143 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 58.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +15.9) | — |
| [[SW1417 (line)]] | alt | 104 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.4) | — |
| [[A498 (line)]] | wt | 167 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.3) | — |
| [[C32 (line)]] | wt | 176 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.4) | — |
| [[LoVo (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.483× (z -9.8) ⚠ cell-cycle shift, explains ~78% of this change |
| [[LOX-IMVI (line)]] | wt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 199 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +15.5) | — |
| [[NCI-H23 (line)]] | alt | 163 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 86.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +14.3) | — |
| [[RKO (line)]] | wt | 174 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 58.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 94.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 49.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +15.1) | — |
| [[SW480 (line)]] | alt | 114 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +10.9) | — |
| [[A-172 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 159 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 146 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 299 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFRC]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[BZW2]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[AMD1]] | +0.61 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[LGMN]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SNAI1]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[KLHL15]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[UAP1]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SRSF7]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[PTDSS1]] | +0.53 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PREP]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[CSRP2]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SLC16A10]] | +0.51 | +0.37 / +0.50 | both halves | 8e-05 | same gene group; pathway: SLC-mediated transmembrane transport |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN16]] | -0.47 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[SMIM7]] | -0.46 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[PPP6C]] | -0.45 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[MAU2]] | -0.44 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[TSG101]] | -0.44 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[IFT22]] | -0.43 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[CAB39]] | -0.43 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[VPS16]] | -0.43 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[COPS5]] | -0.43 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[SNRNP35]] | -0.42 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[YIPF4]] | -0.42 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[NEK4]] | -0.42 | -0.40 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFAP1-AS1]] | B | AFAP1-AS1 activity lowers SLC16A1's level | lines that do not express AFAP1-AS1 (33) vs lines expressing it (17) | 1.37× higher at baseline in the lines without AFAP1-AS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: AGR2, GABRP, LINC01610 |
| [[POLR3G]] | C | POLR3G activity raises SLC16A1's level | lines that do not express POLR3G (3) vs lines expressing it (47) | 3.44× lower at baseline in the lines without POLR3G | 0.054 | ⚠ few lines (3 vs 47); across organs; also absent: HMGA1, PALS2, SLC35F2; maybe low, not absent; co-absent with the target |
| [[CSPG5]] | C | CSPG5 activity raises SLC16A1's level | lines that do not express CSPG5 (3) vs lines expressing it (47) | 3.26× lower at baseline in the lines without CSPG5 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYGM]] | C | SLC16A1 activity lowers PYGM's level | lines that do not express SLC16A1 (3) vs lines expressing it (47) | 2.19× higher at baseline in the lines without SLC16A1 | 0.047 | ⚠ few lines (3 vs 47); across organs; co-occurs with ERBB2; also absent: SLC16A1-AS1, SLC4A7, PALS2 |
| cells under [[MK-3903 (drug)]] 5 µM | C | SLC16A1 activity raises the cells' numbers under MK-3903 5 µM (protects the cells) | lines that do not express SLC16A1 (3) vs lines expressing it (45) | the lines without SLC16A1: 0.70× the cells of the other lines | 0.065 | ⚠ few lines (3 vs 47); across organs; co-occurs with ERBB2; also absent: SLC16A1-AS1, SLC4A7, PALS2 |
| [[SNRNP35]] | C | SLC16A1 activity lowers SNRNP35's level | lines that do not express SLC16A1 (3) vs lines expressing it (47) | 1.44× higher at baseline in the lines without SLC16A1 | 0.098 | ⚠ few lines (3 vs 47); across organs; co-occurs with ERBB2; also absent: SLC16A1-AS1, SLC4A7, PALS2 |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.9, 6.0); signed map (-46.4, 25.3). **Vector** length 105, 32.8% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +14.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.0 | +3.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.5 | +5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +2.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.8 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 16 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:112,911,847-112,957,593 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCT, MCT1 |
| Gene groups (HGNC) | Solute carrier family 16 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 11 pathways, smallest: Proton-coupled monocarboxylate transport; Aspirin ADME; Basigin interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P53985](https://www.uniprot.org/uniprotkb/P53985) (Monocarboxylate transporter 1):

> Bidirectional proton-coupled monocarboxylate transporter. Catalyzes the rapid transport across the plasma membrane of many monocarboxylates such as lactate, pyruvate, acetate and the ketone bodies acetoacetate and beta-hydroxybutyrate, and thus contributes to the maintenance of intracellular pH. The transport direction is determined by the proton motive force and the concentration gradient of the substrate monocarboxylate. MCT1 is a major lactate exporter (By similarity). Plays a role in …

**Summary**, from NCBI Gene [6566](https://www.ncbi.nlm.nih.gov/gene/6566):

> The protein encoded by this gene is a proton-linked monocarboxylate transporter that catalyzes the movement of many monocarboxylates, such as lactate and pyruvate, across the plasma membrane. Mutations in this gene are associated with erythrocyte lactate transporter defect. Alternatively spliced transcript variants have been found for this gene.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:10922](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10922) · Entrez [6566](https://www.ncbi.nlm.nih.gov/gene/6566) · UniProt [P53985](https://www.uniprot.org/uniprotkb/P53985) · Ensembl [ENSG00000155380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155380)

## Data

Gene col 7893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7893); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7893]; `tensor/DDL_lfc|DDL_z.npy` [7893]; `embed/gene_vectors.npy` [7893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7893 or target_col == 7893). Every well: [[SLC16A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC16A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
