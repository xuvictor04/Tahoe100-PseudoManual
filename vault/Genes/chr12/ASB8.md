---
symbol: "ASB8"
type: "gene"
col: 10884
ensembl_id: "ENSG00000177981"
name: "ankyrin repeat and SOCS box containing 8"
location: "12q13.11"
module: 12
arm: "+"
pooled_cpm: 17.02
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ASB8

*ankyrin repeat and SOCS box containing 8* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.69× (z +7.9, q 2e-12, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.446× (z -12.0, q 1e-30, down in 42 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.514× (z -9.9, q 9e-21, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM23]] (+0.79, fdr 7e-06), [[C18orf21]] (+0.76, fdr 7e-06), [[RP9]] (+0.76, fdr 7e-06); moves opposite to [[AHCY]] (-0.65, fdr 7e-06), [[AKT1]] (-0.65, fdr 7e-06), [[UBE2G2]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SUCLG1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +7.9 | 2e-12 | 32/48 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +7.6 | 6e-12 | 29/47 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.38×** | +6.9 | 1e-09 | 27/47 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.4 | 1e-05 | 24/48 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.43×** | +5.2 | 2e-05 | 21/47 (A-427, SW480, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +4.9 | 1e-04 | 18/47 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +4.5 | 6e-04 | 20/48 (PANC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.4 | 7e-04 | 16/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +4.3 | 0.001 | 16/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 0.002 | 18/48 (HEC-1-A, LS 180, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.31×** | +4.1 | 0.003 | 15/44 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.66×** | +4.0 | 0.003 | 15/44 (HCT15, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.004 | 13/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.8 | 0.005 | 15/43 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.031 | 8/48 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.041 | 14/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.056 | 10/47 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.063 | 3/46 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.071 | 10/48 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10884.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.446×** | -12.0 | 1e-30 | 42/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -9.9 | 9e-21 | 38/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.567×** | -8.4 | 6e-15 | 33/48 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.568×** | -8.4 | 6e-15 | 29/46 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.591×** | -7.8 | 6e-13 | 33/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -7.1 | 1e-10 | 28/47 (Hs 766T, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.634×** | -6.8 | 1e-09 | 32/47 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.675×** | -5.8 | 4e-07 | 21/39 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -4.8 | 1e-04 | 21/46 (SNU-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.742×** | -4.3 | 0.001 | 15/30 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.579×** | -4.2 | 0.001 | 20/45 (NCI-H1792, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.751×** | -4.1 | 0.002 | 19/44 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.760×** | -4.1 | 0.002 | 20/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.602×** | -4.0 | 0.003 | 12/48 (CFPAC-1, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.770×** | -3.7 | 0.007 | 18/48 (A-172, RPMI-7951, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.797×** | -3.4 | 0.028 | 16/47 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.799×** | -3.3 | 0.030 | 15/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.667×** | -3.1 | 0.052 | 11/46 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.810×** | -3.1 | 0.052 | 15/46 (MIA PaCa-2, SHP-77, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.2 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.172× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 25.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -9.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 17.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.4) ⚠ cell-cycle shift, explains ~44% of this change | [[Dinaciclib (drug)]] 5 µM 0.209× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 18.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -9.2) |
| [[SW480 (line)]] | alt | 25.0 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.383× (z -9.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.404× (z -8.9) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -9.8) ⚠ cell-cycle shift, explains ~15% of this change |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0777× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -13.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.88 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.161× (z -8.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.206× (z -10.3) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM23]] | +0.79 | +0.82 / +0.73 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[RP9]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[SECISBP2L]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PHAX]] | +0.73 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[CIR1]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[IK]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[KBTBD7]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[DNAL4]] | +0.73 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[CRBN]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[METTL14]] | +0.72 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SNAPIN]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHCY]] | -0.65 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[AKT1]] | -0.65 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[UBE2G2]] | -0.64 | -0.57 / -0.65 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PRPS2]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[ARHGAP4]] | -0.64 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[GART]] | -0.63 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[TTL]] | -0.63 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[SEH1L]] | -0.62 | -0.65 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUCLG1]] | C | ASB8's natural level weakens SUCLG1's drug response | ASB8's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.13; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.821). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.1, -0.2); signed map (-15.7, -8.0). **Vector** length 103, 24.0% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.50 to 17); *mRNA Splicing* (reactome, mean cos +0.50 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.9 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.6 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -12.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and SOCS box containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:48,147,789-48,181,213 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5540, FLJ21255 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H765](https://www.uniprot.org/uniprotkb/Q9H765) (Ankyrin repeat and SOCS box protein 8):

> May be a substrate-recognition component of a SCF-like ECS (Elongin-Cullin-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Inhibits IFN-beta production through the IRF3 signaling pathway by targeting TBK1 via 'Lys-48'-linked ubiquitination, leading to its proteasomal degradation.

**Summary**, from NCBI Gene [140461](https://www.ncbi.nlm.nih.gov/gene/140461):

> Predicted to be involved in intracellular signal transduction and protein ubiquitination. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17183) · Entrez [140461](https://www.ncbi.nlm.nih.gov/gene/140461) · UniProt [Q9H765](https://www.uniprot.org/uniprotkb/Q9H765) · Ensembl [ENSG00000177981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177981)

## Data

Gene col 10884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10884); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10884]; `tensor/DDL_lfc|DDL_z.npy` [10884]; `embed/gene_vectors.npy` [10884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10884 or target_col == 10884). Every well: [[ASB8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASB8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
