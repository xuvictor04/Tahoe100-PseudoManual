---
symbol: "GATD1-DT"
type: "gene"
col: 14930
ensembl_id: "ENSG00000255284"
name: "GATD1 divergent transcript"
location: "11p15.5"
module: 15
arm: "+"
pooled_cpm: 14.39
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# GATD1-DT

*GATD1 divergent transcript* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.46× (z +12.3, q 5e-32, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.440× (z -11.2, q 1e-26, down in 35 of 45 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.373× (z -9.2, q 1e-17, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNB1-DT]] (+0.68, fdr 7e-06), [[SLC12A9]] (+0.65, fdr 1e-05), [[PPP1R26-AS1]] (+0.63, fdr 3e-05); moves opposite to [[ALAS1]] (-0.65, fdr 2e-05), [[PRELID3B]] (-0.56, fdr 4e-05), [[CSRP1]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +12.3 | 5e-32 | 39/46 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +6.0 | 6e-07 | 29/45 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +4.3 | 0.004 | 9/25 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.53×** | +3.7 | 0.037 | 14/46 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.6 | 0.038 | 20/37 (SW1417, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.069 | 10/46 (HT-29, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.069 | 12/48 (Hs 766T, A498, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.39× | +3.2 | 0.10 | 11/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.38× | +3.1 | 0.12 | 12/47 (AN3 CA, J82, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14930.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.440×** | -11.2 | 1e-26 | 35/45 (HEC-1-A, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.373×** | -9.2 | 1e-17 | 39/46 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.392×** | -9.1 | 2e-17 | 42/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.415×** | -8.5 | 2e-15 | 32/45 (LS 180, H4, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.485×** | -7.0 | 2e-10 | 31/44 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.534×** | -6.1 | 1e-07 | 32/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.314×** | -5.9 | 4e-07 | 28/46 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.343×** | -5.4 | 4e-06 | 30/43 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.593×** | -5.1 | 2e-05 | 23/46 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.629×** | -4.5 | 4e-04 | 26/47 (LOX-IMVI, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.650×** | -4.2 | 0.002 | 22/47 (PANC-1, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -3.9 | 0.004 | 19/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.677×** | -3.6 | 0.015 | 17/46 (SW480, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.692×** | -3.6 | 0.015 | 14/47 (A-427, A498, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.718×** | -3.2 | 0.050 | 18/47 (SNU-1, A498, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.699×** | -3.1 | 0.068 | 16/47 (AN3 CA, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.1 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 24.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -21.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -13.0) |
| [[PANC-1 (line)]] | alt | 35.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -12.0) |
| [[SW480 (line)]] | alt | 22.5 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.250× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.161× (z -10.1) |
| [[A-172 (line)]] | wt | 38.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -11.2) |
| [[A-427 (line)]] | wt | 24.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.181× (z -10.0) |
| [[A549 (line)]] | wt | 11.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.11× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 34.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -9.0) |
| [[LoVo (line)]] | wt | 10.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -8.9) |
| [[LS 180 (line)]] | wt | 10.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.0499× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.32 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 0.05 µM 0.0567× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0772× (z -13.5) |
| [[C32 (line)]] | wt | 8.52 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0934× (z -9.1) |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0617× (z -9.9) |
| [[H4 (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0872× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 4.68 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.101× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 8.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 7.28 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 9.60 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0633× (z -9.6) |
| [[SNU-423 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 4.69 | 0 | 1 | — | [[Bicalutamide (drug)]] 0.5 µM 0.0531× (z -8.7) |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNB1-DT]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 | same gene group |
| [[SLC12A9]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[PPP1R26-AS1]] | +0.63 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[LINC00685]] | +0.63 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[ZNF236-DT]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 | same gene group |
| [[ING2-DT]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 | same gene group |
| [[SPESP1]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[KIAA2026]] | +0.62 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[WDR20]] | +0.61 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[MZT2A]] | +0.61 | +0.38 / +0.71 | both halves | 6e-05 |  |
| [[NR2C2]] | +0.61 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[LINC00106]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAS1]] | -0.65 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[PRELID3B]] | -0.56 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[CSRP1]] | -0.56 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ECHS1]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MAPRE2]] | -0.55 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RPAP3]] | -0.55 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[PHF6]] | -0.55 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ZNF184]] | -0.54 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[HLTF]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[NBN]] | -0.53 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[DMXL2]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[CLCN3]] | -0.52 | -0.31 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GATD1-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers GATD1-DT's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[SLC6A16]] | B | SLC6A16 activity raises GATD1-DT's level | lines that do not express SLC6A16 (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without SLC6A16 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, TEAD2, ZNF71; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | GATD1-DT's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | GATD1-DT's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.67 | 0.323 over the table, 0.034 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.0, 21.1); signed map (4.5, 0.4). **Vector** length 72.4, 14.8% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +12.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +2.3 | -3.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | -0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.2 | -11.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -5.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | GATD1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p15.5 — chr11:777,574-785,231 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29907) · Entrez [171391](https://www.ncbi.nlm.nih.gov/gene/171391) · Ensembl [ENSG00000255284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255284)

## Data

Gene col 14930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14930); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14930]; `tensor/DDL_lfc|DDL_z.npy` [14930]; `embed/gene_vectors.npy` [14930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14930 or target_col == 14930). Every well: [[GATD1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATD1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
