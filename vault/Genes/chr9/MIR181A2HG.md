---
symbol: "MIR181A2HG"
type: "gene"
col: 13373
ensembl_id: "ENSG00000224020"
name: "MIR181A2 host gene"
location: "9q33.3"
module: 46
arm: "+"
pooled_cpm: 14.6
n_lines_expressing: 47
n_dd_up: 32
n_dd_down: 21
n_dd_up_clean: 27
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# MIR181A2HG

*MIR181A2 host gene* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.71× (z +10.9, q 5e-25, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.657× (z -6.0, q 8e-07, down in 19 of 44 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00938]] (+0.64, fdr 4e-05), [[TSTD3]] (+0.63, fdr 8e-05), [[MR1]] (+0.61, fdr 5e-05); moves opposite to [[TBC1D16]] (-0.62, fdr 6e-05), [[SND1]] (-0.58, fdr 3e-05), [[KIF21B]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[UNK]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +10.9 | 5e-25 | 29/45 (SK-MEL-2, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +10.9 | 5e-25 | 26/40 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +9.3 | 2e-18 | 32/45 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +8.1 | 9e-14 | 23/41 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +7.7 | 1e-12 | 25/45 (HOP62, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +6.3 | 3e-08 | 21/44 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.47×** | +5.5 | 2e-06 | 15/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.4 | 5e-06 | 19/43 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.55×** | +5.2 | 1e-05 | 14/44 (HOP62, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 2e-04 | 17/44 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +4.5 | 3e-04 | 6/45 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +4.3 | 8e-04 | 12/45 (C32, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.001 | 12/45 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.001 | 12/41 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.001 | 14/41 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.001 | 12/44 (C32, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.657×** | -6.0 | 8e-07 | 19/44 (J82, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.661×** | -5.9 | 8e-07 | 18/44 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.664×** | -5.7 | 3e-06 | 19/41 (HepG2/C3A, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.686×** | -5.4 | 8e-06 | 19/44 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.659×** | -5.0 | 7e-05 | 16/44 (HOP62, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.709×** | -4.9 | 7e-05 | 19/44 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.759×** | -4.0 | 0.006 | 14/44 (NCI-H460, SNU-423, …) | two highest doses |  |
| [[Rimonabant (drug)]] 5 µM |  | **0.827×** | -3.9 | 0.008 | 9/45 (LoVo, CHP-212, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.726×** | -3.8 | 0.009 | 16/45 (NCI-H661, J82, …) | two highest doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.609×** | -3.7 | 0.011 | 12/45 (J82, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.774×** | -3.7 | 0.012 | 9/44 (SK-MEL-2, J82, …) | two highest doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -3.6 | 0.017 | 5/45 (KATO III, AsPC-1, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.782×** | -3.5 | 0.017 | 12/41 (CHP-212, SW 900, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.777×** | -3.5 | 0.020 | 10/45 (PANC-1, RKO, …) | top dose only | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.843× | -3.5 | 0.020 | 7/45 (SHP-77, AsPC-1, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.845× | -3.4 | 0.022 | 9/45 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.751×** | -3.4 | 0.022 | 9/43 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.850× | -3.3 | 0.029 | 16/45 (A498, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.029 | 13/44 (SNU-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.653×** | -3.2 | 0.035 | 10/42 (HEC-1-A, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.656×** | -3.2 | 0.035 | 10/42 (Hs 766T, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 17.4 | 3 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.58× (z +10.9) | — |
| [[C32 (line)]] | wt | 13.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 20.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0901× (z -10.0) ⚠ toxic |
| [[J82 (line)]] | alt | 40.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 29.2 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.221× (z -8.7) |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0479× (z -9.3) |
| [[H4 (line)]] | wt | 21.8 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.115× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 24.8 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.92× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.135× (z -9.3) |
| [[KATO III (line)]] | alt | 6.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.93 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.85× (z +8.8) ⚠ position not correctable | — |
| [[NCI-H23 (line)]] | alt | 29.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.183× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0568× (z -9.7) ⚠ toxic |
| [[RKO (line)]] | wt | 4.40 | 0 | 1 | — | [[Relugolix (drug)]] 0.05 µM 0.0392× (z -9.3) |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 30.0 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.54× (z +8.8) | — |
| [[A-172 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00938]] | +0.64 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[TSTD3]] | +0.63 | +0.60 / +0.37 | both halves | 8e-05 |  |
| [[MR1]] | +0.61 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[TTC32]] | +0.60 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[ZNF821]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[C3orf38]] | +0.60 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[PIGP]] | +0.60 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PNISR-AS1]] | +0.59 | +0.61 / +0.21 | both halves | 7e-04 |  |
| [[CASD1]] | +0.59 | +0.52 / +0.28 | both halves | 3e-04 |  |
| [[TP53]] | +0.59 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[ANKRA2]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ZNF226]] | +0.58 | +0.52 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D16]] | -0.62 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[SND1]] | -0.58 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[KIF21B]] | -0.58 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[SLC45A4]] | -0.57 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SPTLC2]] | -0.57 | -0.61 / -0.26 | both halves | 4e-04 |  |
| [[GPRIN1]] | -0.56 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[RSU1]] | -0.56 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[EP400]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[CAP1]] | -0.55 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ST6GALNAC4]] | -0.55 | -0.46 / -0.24 | both halves | 4e-04 |  |
| [[FARP2]] | -0.55 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[CDC42BPB]] | -0.54 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MIR181A2HG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01139]] | B | LINC01139 activity raises MIR181A2HG's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 1.89× lower at baseline in the lines without LINC01139 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNK]] | C | MIR181A2HG activity raises UNK's level | lines that do not express MIR181A2HG (3) vs lines expressing it (47) | 1.29× lower at baseline in the lines without MIR181A2HG | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: APOBEC3C, VAT1, CAPRIN2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (1.0, 17.5); signed map (24.7, -14.0). **Vector** length 86.5, 17.3% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.5 | +10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +10.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.1 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +7.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +9.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +3.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -5.0 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.8 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.4 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.2 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | MIR181A2 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q33.3 — chr9:124,658,412-124,698,635 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:37188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37188) · Entrez [100379345](https://www.ncbi.nlm.nih.gov/gene/100379345) · Ensembl [ENSG00000224020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224020)

## Data

Gene col 13373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13373); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13373]; `tensor/DDL_lfc|DDL_z.npy` [13373]; `embed/gene_vectors.npy` [13373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13373 or target_col == 13373). Every well: [[MIR181A2HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR181A2HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
