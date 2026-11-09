---
symbol: "HAPLN3"
type: "gene"
col: 6421
ensembl_id: "ENSG00000140511"
name: "hyaluronan and proteoglycan link protein 3"
location: "15q26.1"
module: 21
arm: "+"
pooled_cpm: 7.88
n_lines_expressing: 43
n_dd_up: 25
n_dd_down: 17
n_dd_up_clean: 21
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# HAPLN3

*hyaluronan and proteoglycan link protein 3* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.57× (z +26.2, q 0e+00, up in 33 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.601× (z -6.2, q 3e-07, down in 20 of 40 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.461× (z -4.9, q 2e-04, down in 10 of 31 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFGE8]] (+0.68, fdr 1e-05, ⚠ same locus), [[PDE4A]] (+0.59, fdr 6e-05), [[MEIS3]] (+0.56, fdr 4e-05), [[DISP3]] (+0.56, fdr 1e-05); moves opposite to [[PTCD2]] (-0.51, fdr 2e-04), [[ZFP62]] (-0.50, fdr 3e-05), [[MRPS27]] (-0.49, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[CST3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.57×** | +26.2 | 0e+00 | 33/34 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.62×** | +15.7 | 0e+00 | 35/40 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.42×** | +15.2 | 0e+00 | 36/40 (SW480, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.37×** | +14.8 | 0e+00 | 36/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.35×** | +14.2 | 1e-43 | 27/35 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +13.6 | 2e-40 | 26/34 (CFPAC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.77×** | +12.4 | 1e-33 | 33/40 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.32×** | +10.3 | 8e-23 | 33/40 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +9.7 | 2e-20 | 31/38 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +9.6 | 4e-20 | 23/33 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +7.3 | 2e-11 | 18/27 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +5.2 | 1e-05 | 16/38 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +5.1 | 2e-05 | 9/39 (A498, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.8 | 6e-05 | 12/40 (A-172, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.8 | 6e-05 | 15/39 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +4.8 | 6e-05 | 15/34 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -6.2 | 3e-07 | 20/40 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.461×** | -4.9 | 2e-04 | 10/31 (A549, NCI-H23, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.662×** | -4.9 | 2e-04 | 13/36 (A-172, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.677×** | -4.8 | 2e-04 | 16/38 (hTERT-HPNE, HOP62, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.474×** | -4.8 | 2e-04 | 16/36 (NCI-H460, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.742×** | -3.7 | 0.024 | 9/40 (AN3 CA, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **0.746×** | -3.6 | 0.027 | 11/36 (hTERT-HPNE, HCT15, …) | inconsistent across doses | position effect removed |
| [[Drospirenone (drug)]] 0.5 µM |  | **0.753×** | -3.5 | 0.036 | 13/36 (LoVo, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.762×** | -3.3 | 0.052 | 10/38 (NCI-H2030, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.763×** | -3.3 | 0.052 | 14/36 (HCT15, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.765×** | -3.3 | 0.054 | 9/39 (SW48, C-33 A, …) | top dose only | position effect removed |
| [[Fumaric acid (drug)]] 0.05 µM |  | **0.754×** | -3.2 | 0.064 | 10/38 (A549, SW480, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.774×** | -3.1 | 0.075 | 10/32 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.764×** | -3.0 | 0.093 | 10/33 (hTERT-HPNE, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Penfluridol (drug)]] 5 µM |  | **0.775×** | -3.0 | 0.093 | 8/37 (A-427, SW48, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.625×** | -3.0 | 0.093 | 7/35 (NCI-H460, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.76 | 11 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +16.0) | — |
| [[SW480 (line)]] | alt | 4.76 | 7 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +12.9) | [[Harringtonine (drug)]] 0.5 µM 0.169× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 10.8 | 5 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0972× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 13.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.20× (z +14.7) | [[Docetaxel (drug)]] 0.05 µM 0.0772× (z -12.6) ⚠ transcription drop; cell-cycle shift, explains ~16% of this change |
| [[CFPAC-1 (line)]] | alt | 8.21 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +12.9) | [[Docetaxel (drug)]] 0.05 µM 0.126× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~16% of this change |
| [[HOP62 (line)]] | alt | 10.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 20.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.5) | — |
| [[A-172 (line)]] | wt | 11.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +16.1) | [[Cobimetinib (drug)]] 0.05 µM 0.133× (z -9.1) |
| [[A549 (line)]] | wt | 21.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.151× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[HEC-1-A (line)]] | alt | 10.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.65× (z +13.8) | — |
| [[LoVo (line)]] | wt | 8.97 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 2.87 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 7.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 4.19 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.8× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 7.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 5.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +8.6) | — |
| [[A-427 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFGE8]] | +0.68 | +0.54 / +0.78 | both halves | 1e-05 | STRING 526; ⚠ same locus (3.1 kb, same strand: neighbours can correlate without regulation) |
| [[PDE4A]] | +0.59 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[MEIS3]] | +0.56 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[DISP3]] | +0.56 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[AKAP13-AS1]] | +0.55 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[CRLF1]] | +0.55 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[GCH1]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[SAT1]] | +0.53 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[INSR]] | +0.53 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[PPM1N]] | +0.52 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[KCNB1]] | +0.52 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[CRISPLD2]] | +0.51 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[SORCS3]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCD2]] | -0.51 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ZFP62]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[MRPS27]] | -0.49 | -0.47 / -0.43 | both halves | 4e-05 |  |
| [[COG8]] | -0.48 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[MANBAL]] | -0.47 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TOP3B]] | -0.47 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ELMOD2]] | -0.47 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[TSEN15]] | -0.47 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[VPS50]] | -0.47 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[AIFM1]] | -0.47 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[RFT1]] | -0.47 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[MRPL19]] | -0.46 | -0.48 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HAPLN3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SAT1]] | B | SAT1 activity raises HAPLN3's level | lines that do not express SAT1 (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without SAT1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ITPR3, SQOR, KDELR3; maybe low, not absent; its own permutation p |
| [[MFGE8]] | C | MFGE8 activity raises HAPLN3's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 3.19× lower at baseline in the lines without MFGE8 | 0.003 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CST3]] | B | HAPLN3 activity weakens CST3's drug response | lines that do not express HAPLN3 (7) vs lines expressing it (41) | the lines without HAPLN3 respond 1.19× as strongly (z diff -1.08); strongest at Homoharringtonine 5 µM: 0.27x vs 0.42x (z diff -2.6) | 0.086 | ⚠ within organs, on part of the lines; also absent: GLIPR2, MFGE8, GLI2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MFGE8]] | C | HAPLN3 activity raises MFGE8's level | lines that do not express HAPLN3 (7) vs lines expressing it (43) | 3.67× lower at baseline in the lines without HAPLN3 | 0.009 | ⚠ within organs, on part of the lines; also absent: GLIPR2, MFGE8, GLI2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.436). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.1, 36.9); signed map (21.0, 20.0). **Vector** length 75.7, 13.9% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +15.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +26.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +13.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +9.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | hyaluronan and proteoglycan link protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:88,877,294-88,895,597 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HsT19883; previously EXLD1 |
| Gene groups (HGNC) | V-set domain containing; Hyaluronan and proteoglycan link protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S86](https://www.uniprot.org/uniprotkb/Q96S86) (Hyaluronan and proteoglycan link protein 3):

> May function in hyaluronic acid binding.

**Summary**, from NCBI Gene [145864](https://www.ncbi.nlm.nih.gov/gene/145864):

> This gene belongs to the hyaluronan and proteoglycan binding link protein gene family. The protein encoded by this gene may function in hyaluronic acid binding and cell adhesion. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21446) · Entrez [145864](https://www.ncbi.nlm.nih.gov/gene/145864) · UniProt [Q96S86](https://www.uniprot.org/uniprotkb/Q96S86) · Ensembl [ENSG00000140511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140511)

## Data

Gene col 6421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6421); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6421]; `tensor/DDL_lfc|DDL_z.npy` [6421]; `embed/gene_vectors.npy` [6421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6421 or target_col == 6421). Every well: [[HAPLN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAPLN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
