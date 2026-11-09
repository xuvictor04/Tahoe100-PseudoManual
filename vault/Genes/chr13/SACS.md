---
symbol: "SACS"
type: "gene"
col: 7571
ensembl_id: "ENSG00000151835"
name: "sacsin molecular chaperone"
location: "13q12.12"
module: 4
arm: "+"
pooled_cpm: 71.4
n_lines_expressing: 45
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 22
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SACS

*sacsin molecular chaperone* — 13q12.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.68× (z +7.4, q 1e-10, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.515× (z -13.3, q 1e-37, down in 40 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM185B]] (+0.67, fdr 7e-06), [[CCT5]] (+0.66, fdr 7e-06), [[GNPNAT1]] (+0.64, fdr 1e-05); moves opposite to [[COG7]] (-0.68, fdr 7e-06), [[SMIM27]] (-0.62, fdr 8e-06), [[ZNF490]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HEG1]] → it (grade B ⚠); 22 go from it, the strongest it → [[MAPKAPK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +7.4 | 1e-10 | 31/43 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +7.2 | 2e-10 | 32/43 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +6.6 | 6e-09 | 32/43 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +6.1 | 1e-07 | 30/43 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.57×** | +6.1 | 2e-07 | 31/42 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.45×** | +5.3 | 1e-05 | 26/43 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 4e-05 | 24/43 (A498, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.44×** | +5.0 | 4e-05 | 29/42 (SW 900, NCI-H1792, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +5.0 | 4e-05 | 24/43 (SW 900, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.5 | 4e-04 | 26/43 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 4e-04 | 28/43 (A498, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.3 | 9e-04 | 24/42 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.002 | 22/42 (NCI-H460, NCI-H1792, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.004 | 24/43 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +3.8 | 0.005 | 19/43 (A-427, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.007 | 24/43 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.008 | 22/43 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.009 | 20/43 (NCI-H1792, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.009 | 23/43 (LOX-IMVI, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.029 | 19/43 (A498, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7571.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.515×** | -13.3 | 1e-37 | 40/43 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -6.0 | 7e-07 | 34/44 (A-427, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -5.4 | 1e-05 | 23/43 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.598×** | -5.2 | 3e-05 | 31/43 (Hs 766T, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.712×** | -4.8 | 2e-04 | 25/43 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.701×** | -3.6 | 0.031 | 24/43 (RKO, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -3.4 | 0.056 | 19/43 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.848× | -3.3 | 0.064 | 16/43 (LS 180, A-427, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.722×** | -3.3 | 0.064 | 18/43 (C32, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.649×** | -3.2 | 0.076 | 21/43 (A-427, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.730×** | -3.2 | 0.076 | 17/43 (SW 1271, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 175 | 1 (1 ⚠) | 6 (4 ⚠) | [[Selinexor (drug)]] 5 µM 2.01× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -19.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.139× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 72.9 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -15.7) |
| [[HOP62 (line)]] | alt | 94.5 | 1 | 4 | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -13.6) |
| [[A498 (line)]] | wt | 130 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 37.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 82.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.3) |
| [[SNU-423 (line)]] | alt | 99.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.2) |
| [[A-172 (line)]] | wt | 162 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.1) |
| [[C-33 A (line)]] | alt | 80.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[C32 (line)]] | wt | 60.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 19.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -10.0) |
| [[J82 (line)]] | alt | 153 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.1) |
| [[LoVo (line)]] | wt | 30.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.38× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 144 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.0) |
| [[LS 180 (line)]] | wt | 18.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.73× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 88.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 25.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.36× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 73.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -11.5) |
| [[RKO (line)]] | wt | 82.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -8.9) |
| [[SHP-77 (line)]] | alt | 95.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 58.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -10.3) |
| [[SW 1088 (line)]] | alt | 61.2 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0628× (z -8.5) |
| [[SW 1271 (line)]] | alt | 61.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0629× (z -9.0) |
| [[SW 900 (line)]] | alt | 42.5 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.20× (z +8.8) | — |
| [[SW480 (line)]] | alt | 75.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -9.1) |
| [[A549 (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.56 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | +0.67 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[CCT5]] | +0.66 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[GNPNAT1]] | +0.64 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[CCT2]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[GLO1]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[POGK]] | +0.61 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[PANK3]] | +0.60 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[TAF1B]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[CCT3]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[G3BP1]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[TUSC3]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[NBPF20]] | +0.57 | +0.49 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG7]] | -0.68 | -0.69 / -0.65 | both halves | 7e-06 |  |
| [[SMIM27]] | -0.62 | -0.61 / -0.57 | both halves | 8e-06 |  |
| [[ZNF490]] | -0.62 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[NDUFC1]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[ZNF821]] | -0.62 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[KLC4]] | -0.61 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[CCDC115]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[DNAJC4]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 | same gene group |
| [[EOGT-DT]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[WBP1]] | -0.58 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | -0.58 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[NAA38]] | -0.58 | -0.45 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises SACS's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 3.46× lower at baseline in the lines without HEG1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[DHRS3]] | B | DHRS3 activity lowers SACS's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.67× higher at baseline in the lines without DHRS3 | 0.026 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[TOP2A]] | B | TOP2A activity raises SACS's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FSD1L]] | C | FSD1L activity raises SACS's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 4.28× lower at baseline in the lines without FSD1L | 0.022 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[PALM2AKAP2]] | C | PALM2AKAP2 activity raises SACS's level | lines that do not express PALM2AKAP2 (9) vs lines expressing it (41) | 3.07× lower at baseline in the lines without PALM2AKAP2 | 0.037 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MPP1, LIX1L; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPKAPK3]] | B | SACS activity raises MAPKAPK3's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without SACS | 0.011 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[RRP1B]] | B | SACS activity raises RRP1B's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without SACS | 0.012 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[G3BP1]] | B | SACS activity raises G3BP1's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without SACS | 0.024 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[KCNQ5]] | B | SACS activity raises KCNQ5's level | lines that do not express SACS (5) vs lines expressing it (45) | 3.31× lower at baseline in the lines without SACS | 0.034 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[GNPNAT1]] | B | SACS activity raises GNPNAT1's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without SACS | 0.035 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[C12orf29]] | B | SACS activity raises C12orf29's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without SACS | 0.042 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[BEX3]] | B | SACS activity raises BEX3's level | lines that do not express SACS (5) vs lines expressing it (45) | 4.07× lower at baseline in the lines without SACS | 0.047 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[YWHAH]] | B | SACS activity raises YWHAH's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without SACS | 0.053 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[TTL]] | B | SACS activity raises TTL's level | lines that do not express SACS (5) vs lines expressing it (45) | 2.54× lower at baseline in the lines without SACS | 0.058 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[FSD1L]] | B | SACS activity raises FSD1L's level | lines that do not express SACS (5) vs lines expressing it (45) | 3.62× lower at baseline in the lines without SACS | 0.058 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[TTI2]] | B | SACS activity raises TTI2's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without SACS | 0.062 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[HEG1]] | B | SACS activity raises HEG1's level | lines that do not express SACS (5) vs lines expressing it (45) | 4.68× lower at baseline in the lines without SACS | 0.069 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.7, -32.5); signed map (-12.0, -45.0). **Vector** length 137, 42.0% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.4 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | +6.6 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +4.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +6.4 | +6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.2 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.4 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +4.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.1 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -13.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.3 | -6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | sacsin molecular chaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.12 — chr13:23,288,689-23,433,763 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARSACS, KIAA0730, DKFZp686B15167, DNAJC29, SPAX6, PPP1R138 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZJ4](https://www.uniprot.org/uniprotkb/Q9NZJ4) (Sacsin):

> Co-chaperone which acts as a regulator of the Hsp70 chaperone machinery and may be involved in the processing of other ataxia-linked proteins.

**Summary**, from NCBI Gene [26278](https://www.ncbi.nlm.nih.gov/gene/26278):

> This gene encodes the sacsin protein, which includes a UbL domain at the N-terminus, a DnaJ domain, and a HEPN domain at the C-terminus. The gene is highly expressed in the central nervous system, also found in skin, skeletal muscles and at low levels in the pancreas. This gene includes a very large exon spanning more than 12.8 kb. Mutations in this gene result in autosomal recessive spastic ataxia of Charlevoix-Saguenay (ARSACS), a neurodegenerative disorder characterized by early-onset …

**Accessions** — [HGNC:10519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10519) · Entrez [26278](https://www.ncbi.nlm.nih.gov/gene/26278) · UniProt [Q9NZJ4](https://www.uniprot.org/uniprotkb/Q9NZJ4) · Ensembl [ENSG00000151835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151835)

## Data

Gene col 7571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7571); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7571]; `tensor/DDL_lfc|DDL_z.npy` [7571]; `embed/gene_vectors.npy` [7571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7571 or target_col == 7571). Every well: [[SACS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SACS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
