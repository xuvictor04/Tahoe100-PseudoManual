---
symbol: "MRPS25"
type: "gene"
col: 5195
ensembl_id: "ENSG00000131368"
name: "mitochondrial ribosomal protein S25"
location: "3p25.1"
module: 18
arm: "+"
pooled_cpm: 36.93
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MRPS25

*mitochondrial ribosomal protein S25* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.31× (z +18.0, q 0e+00, up in 38 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +15.0, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.512× (z -7.9, q 2e-12, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC1]] (+0.76, fdr 7e-06), [[UBE2G2]] (+0.73, fdr 7e-06), [[METTL3]] (+0.72, fdr 9e-06); moves opposite to [[RNASE4]] (-0.64, fdr 1e-05), [[ZNF184]] (-0.64, fdr 2e-05), [[AFTPH]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NCS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +18.0 | 0e+00 | 38/41 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +16.4 | 0e+00 | 39/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +15.0 | 0e+00 | 39/48 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.89×** | +14.2 | 1e-43 | 46/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +13.7 | 2e-40 | 38/45 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.78×** | +12.5 | 1e-33 | 42/47 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.69×** | +11.3 | 1e-27 | 29/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.60×** | +10.5 | 7e-24 | 36/48 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.47×** | +8.7 | 3e-16 | 34/48 (A-172, HOP62, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.05×** | +8.4 | 2e-15 | 38/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +8.1 | 3e-14 | 32/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.41×** | +7.6 | 1e-12 | 32/47 (J82, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.88×** | +7.4 | 6e-12 | 35/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.82×** | +7.0 | 9e-11 | 32/48 (HEC-1-A, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +6.9 | 2e-10 | 29/48 (HS-578T, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.71×** | +6.3 | 1e-08 | 27/48 (A-427, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +5.8 | 2e-07 | 26/47 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 4e-05 | 18/47 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.47×** | +4.5 | 2e-04 | 19/46 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.003 | 14/47 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.004 | 13/48 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.005 | 11/48 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.006 | 5/48 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.011 | 8/48 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.4 | 0.011 | 13/48 (HS-578T, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5195.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.512×** | -7.9 | 2e-12 | 34/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.572×** | -6.6 | 1e-08 | 26/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.852× | -5.1 | 5e-05 | 15/48 (LS 180, SW480, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.820×** | -4.5 | 1e-03 | 11/48 (A-427, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.849× | -3.6 | 0.039 | 16/48 (RKO, NCI-H23, …) | top dose only | composition shift |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.851× | -3.4 | 0.065 | 11/47 (C32, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 52.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.0) | [[Lonafarnib (drug)]] 5 µM 0.0873× (z -16.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 36.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.38× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 32.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.2) | — |
| [[A-427 (line)]] | wt | 47.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.11× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 26.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 27.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 46.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +10.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 30.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 34.8 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +12.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 20.4 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.89× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~25% of this change | — |
| [[LoVo (line)]] | wt | 51.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.75× (z +16.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 33.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +12.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 54.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +9.5) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 5 µM 0.293× (z -8.6) |
| [[A-172 (line)]] | wt | 37.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.6) | — |
| [[A498 (line)]] | wt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 42.9 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0870× (z -11.2) |
| [[C-33 A (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.299× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 30.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 47.9 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0926× (z -10.8) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 42.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.18× (z +10.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 63.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -17.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.73× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC1]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[UBE2G2]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 | STRING 478 |
| [[METTL3]] | +0.72 | +0.57 / +0.74 | both halves | 9e-06 |  |
| [[SEH1L]] | +0.72 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.70 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.69 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[WDR12]] | +0.68 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.68 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[PUM3]] | +0.67 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[METTL8]] | +0.67 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[LETM1]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[MDN1]] | +0.66 | +0.66 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASE4]] | -0.64 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[ZNF184]] | -0.64 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[AFTPH]] | -0.62 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[DBP]] | -0.60 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ASB8]] | -0.60 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SNAPIN]] | -0.60 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[KMT2A]] | -0.60 | -0.40 / -0.71 | both halves | 5e-05 |  |
| [[POLD4]] | -0.58 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[DCTN3]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[IK]] | -0.57 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[KDM5B]] | -0.57 | -0.57 / -0.57 | both halves | 9e-06 |  |
| [[CIR1]] | -0.57 | -0.47 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCS1]] | B | NCS1 activity raises MRPS25's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.00× lower at baseline in the lines without NCS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[DUXAP8]] | B | DUXAP8 activity raises MRPS25's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without DUXAP8 | 0.091 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[CCDC34]] | C | CCDC34's natural level strengthens MRPS25's drug response | CCDC34's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.37; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.9, -36.5); signed map (-2.8, -51.5). **Vector** length 96.9, 23.8% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.1 | +14.2 |
|  | [[EX229 (drug)]] 5 µM |  | +5.6 | +8.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +5.4 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.2 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.1 | +6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.6 | +7.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.5 | +7.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.5 | +3.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.7 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.7 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.9 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:15,009,611-15,065,339 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-S25, FLJ00023, DKFZp313H0817, RPMS25, mS25 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [P82663](https://www.uniprot.org/uniprotkb/P82663) carries no function annotation.

**Summary**, from NCBI Gene [64432](https://www.ncbi.nlm.nih.gov/gene/64432):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14511](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14511) · Entrez [64432](https://www.ncbi.nlm.nih.gov/gene/64432) · UniProt [P82663](https://www.uniprot.org/uniprotkb/P82663) · Ensembl [ENSG00000131368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131368)

## Data

Gene col 5195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5195); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5195]; `tensor/DDL_lfc|DDL_z.npy` [5195]; `embed/gene_vectors.npy` [5195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5195 or target_col == 5195). Every well: [[MRPS25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
