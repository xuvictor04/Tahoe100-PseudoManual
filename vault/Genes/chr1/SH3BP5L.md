---
symbol: "SH3BP5L"
type: "gene"
col: 10567
ensembl_id: "ENSG00000175137"
name: "SH3 binding domain protein 5 like"
location: "1q44"
module: 142
arm: "+"
pooled_cpm: 10.57
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# SH3BP5L

*SH3 binding domain protein 5 like* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.19× (z +10.3, q 6e-22, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.638× (z -8.7, q 2e-15, down in 27 of 44 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.522× (z -7.1, q 4e-10, down in 28 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 20 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.109×, A-172 0.201×, J82 0.209×, HOP62 0.291×; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.129×; ⚠ cell-cycle shift, explains ~26% of this change); [[Oxaprozin (drug)]] 0.5 µM in 1 line (SHP-77 0.0607×); [[Radotinib (drug)]] 5 µM in 1 line (RKO 0.295×); [[Binimetinib (drug)]] 0.5 µM in 1 line (RKO 0.245×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGS1]] (+0.65, fdr 7e-06), [[ERCC3]] (+0.64, fdr 7e-06), [[ZNF384]] (+0.64, fdr 1e-05); moves opposite to [[LGALS3]] (-0.55, fdr 1e-05), [[VPS13C]] (-0.53, fdr 1e-05), [[ROBO1]] (-0.51, fdr 2e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LGALS3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RGMB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.19×** | +10.3 | 6e-22 | 38/47 (A-427, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.46×** | +8.9 | 2e-16 | 31/43 (HOP62, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +6.9 | 8e-10 | 26/47 (A-172, NCI-H2030, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.40×** | +6.5 | 1e-08 | 20/48 (PANC-1, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +4.9 | 1e-04 | 17/45 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.46×** | +4.9 | 1e-04 | 23/44 (A-172, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 8e-04 | 9/41 (NCI-H1792, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.36×** | +4.2 | 0.002 | 15/47 (A-172, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.002 | 17/44 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.005 | 13/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +3.7 | 0.009 | 13/47 (NCI-H1573, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.010 | 15/47 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.014 | 9/47 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +3.5 | 0.018 | 10/47 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.3 | 0.035 | 10/31 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.053 | 6/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.059 | 9/47 (NCI-H23, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.064 | 3/47 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.064 | 9/47 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.072 | 11/46 (HOP62, A-172, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.088 | 5/44 (SK-MEL-2, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10567.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 20 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.109×, A-172 0.201×, J82 0.209×, HOP62 0.291×; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.129×; ⚠ cell-cycle shift, explains ~26% of this change); [[Oxaprozin (drug)]] 0.5 µM in 1 line (SHP-77 0.0607×); [[Radotinib (drug)]] 5 µM in 1 line (RKO 0.295×); [[Binimetinib (drug)]] 0.5 µM in 1 line (RKO 0.245×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.638×** | -8.7 | 2e-15 | 27/44 (RKO, A-172, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.522×** | -7.1 | 4e-10 | 28/46 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.670×** | -5.2 | 4e-05 | 20/46 (RKO, H4, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.694×** | -4.8 | 3e-04 | 21/34 (RKO, PANC-1, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.722×** | -4.5 | 9e-04 | 16/42 (RKO, A-172, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.758× | -3.2 | 0.14 | 1/47 (A-172) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | 0.758× | -3.0 | 0.20 | 11/39 (SHP-77, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 59.2 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -21.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.295× (z -11.8) |
| [[A-172 (line)]] | wt | 18.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -13.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 9.49 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0607× (z -11.9) |
| [[C-33 A (line)]] | alt | 8.75 | 0 | 1 | — | [[Captopril (drug)]] 0.5 µM 0.0876× (z -9.0) |
| [[H4 (line)]] | wt | 11.6 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 0.05 µM 0.0478× (z -10.3) |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.113× (z -8.5) |
| [[Hs 766T (line)]] | wt | 8.72 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.149× (z -8.5) |
| [[J82 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LOX-IMVI (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 5.00 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.104× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 7.87 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.197× (z -8.8) |
| [[SW480 (line)]] | alt | 7.80 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGS1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ERCC3]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ZNF384]] | +0.64 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[STARD3]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[THOC5]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CSK]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[EIF1AD]] | +0.58 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[CHPF2]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[C1orf52]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RIC8A]] | +0.56 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[SNHG21]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[CTU1]] | +0.53 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS3]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[VPS13C]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ROBO1]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[LINC01473]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[SETDB2]] | -0.50 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[REL]] | -0.49 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[MAK]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SMCHD1]] | -0.47 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[LMNA]] | -0.47 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ZC3H6]] | -0.47 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[NUCKS1]] | -0.47 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[PER2]] | -0.47 | -0.31 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3]] | B | LGALS3 activity lowers SH3BP5L's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.33× higher at baseline in the lines without LGALS3 | 0.072 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGMB]] | C | SH3BP5L's natural level weakens RGMB's drug response | SH3BP5L's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.40; direction not clear | 0.057 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.5, -9.5); signed map (-34.1, -27.6). **Vector** length 83.7, 15.2% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.0 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.6 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.5 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.0 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SH3 binding domain protein 5 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:248,810,446-248,825,915 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1720 |
| Gene groups (HGNC) | SH3 domain binding protein 5 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L8J4](https://www.uniprot.org/uniprotkb/Q7L8J4) (SH3 domain-binding protein 5-like):

> Functions as a guanine nucleotide exchange factor (GEF) for RAB11A.

**Summary**, from NCBI Gene [80851](https://www.ncbi.nlm.nih.gov/gene/80851):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in intracellular signal transduction. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29360) · Entrez [80851](https://www.ncbi.nlm.nih.gov/gene/80851) · UniProt [Q7L8J4](https://www.uniprot.org/uniprotkb/Q7L8J4) · Ensembl [ENSG00000175137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175137)

## Data

Gene col 10567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10567); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10567]; `tensor/DDL_lfc|DDL_z.npy` [10567]; `embed/gene_vectors.npy` [10567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10567 or target_col == 10567). Every well: [[SH3BP5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3BP5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
