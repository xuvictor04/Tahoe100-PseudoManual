---
symbol: "TM4SF1-AS1"
type: "gene"
col: 14240
ensembl_id: "ENSG00000240541"
name: "TM4SF1 antisense RNA 1"
location: "3q25.1"
module: 112
arm: "+"
pooled_cpm: 4.58
n_lines_expressing: 36
n_dd_up: 18
n_dd_down: 36
n_dd_up_clean: 13
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# TM4SF1-AS1

*TM4SF1 antisense RNA 1* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.70× (z +7.4, q 7e-11, up in 16 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.236× (z -14.2, q 6e-43, down in 27 of 33 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA2-AS1]] (+0.59, fdr 2e-05), [[HCG20]] (+0.56, fdr 1e-04), [[CLDN16]] (+0.56, fdr 5e-05); moves opposite to [[COPS8]] (-0.44, fdr 5e-05), [[TRAM2]] (-0.44, fdr 2e-04), [[PRKAR2A]] (-0.44, fdr 2e-04).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DPF3]] → it (grade B ⚠); 4 go from it, the strongest it → [[NABP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.4 | 7e-11 | 16/33 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +6.7 | 5e-09 | 7/11 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +5.2 | 4e-05 | 12/32 (CFPAC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.0 | 8e-05 | 8/29 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.51×** | +4.7 | 2e-04 | 2/9 (MIA PaCa-2, NCI-H23) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +4.7 | 2e-04 | 11/32 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.67×** | +4.7 | 2e-04 | 12/26 (A549, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.32×** | +3.9 | 0.007 | 11/33 (A-427, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.017 | 6/33 (SNU-423, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.018 | 6/33 (NCI-H1792, hTERT-HPNE, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.6 | 0.018 | 6/22 (A-427, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.4 | 0.038 | 1/18 (A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.042 | 3/33 (HT-29, SW480, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.056 | 2/33 (SW480, HEC-1-A) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.060 | 2/33 (MIA PaCa-2, NCI-H23) | top dose only |  |
| [[Methotrexate (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.063 | 2/33 (NCI-H460, A549) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.088 | 8/33 (SW1417, A-427, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Lonafarnib (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.096 | 3/33 (SNU-1, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14240.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.236×** | -14.2 | 6e-43 | 27/33 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.290×** | -12.2 | 1e-31 | 27/33 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.377×** | -9.6 | 2e-19 | 23/33 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.428×** | -8.0 | 2e-13 | 20/31 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.628×** | -6.4 | 1e-08 | 19/29 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.574×** | -5.4 | 5e-06 | 16/27 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **0.617×** | -4.7 | 2e-04 | 13/33 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.618×** | -4.7 | 2e-04 | 15/33 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.624×** | -4.6 | 2e-04 | 13/33 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.632×** | -4.5 | 4e-04 | 14/33 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.653×** | -4.2 | 0.002 | 11/33 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.664×** | -4.0 | 0.003 | 12/33 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.673×** | -3.9 | 0.005 | 11/32 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.677×** | -3.8 | 0.005 | 11/33 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.678×** | -3.8 | 0.005 | 8/33 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.682×** | -3.7 | 0.006 | 15/29 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.689×** | -3.4 | 0.026 | 8/28 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.2) |
| [[PANC-1 (line)]] | alt | 7.30 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -13.2) |
| [[COLO 205 (line)]] | alt | 8.06 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0565× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0757× (z -11.1) |
| [[A549 (line)]] | wt | 9.45 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 3.77 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0587× (z -8.7) |
| [[HT-29 (line)]] | alt | 9.13 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0880× (z -10.2) |
| [[KATO III (line)]] | alt | 8.61 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 3.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 7.07 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0900× (z -8.8) |
| [[A-172 (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.884 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA2-AS1]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 | same gene group |
| [[HCG20]] | +0.56 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[CLDN16]] | +0.56 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[DLGAP1-AS1]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[TM4SF1]] | +0.54 | +0.48 / +0.67 | both halves | 2e-05 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[LINC01010]] | +0.53 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[LINC00513]] | +0.52 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[RNF215]] | +0.52 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[CXCL8]] | +0.52 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[BHLHE40-AS1]] | +0.52 | +0.39 / +0.46 | both halves | 6e-05 | same gene group |
| [[CXCL1]] | +0.51 | +0.32 / +0.45 | both halves | 2e-04 |  |
| [[FAM107B]] | +0.50 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[MYOM1]] | +0.50 | +0.52 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS8]] | -0.44 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[TRAM2]] | -0.44 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[PRKAR2A]] | -0.44 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[SKIC3]] | -0.42 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[ESD]] | -0.41 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[CAPN7]] | -0.41 | -0.22 / -0.42 | both halves | 6e-04 |  |
| [[CS]] | -0.41 | -0.24 / -0.35 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPF3]] | B | DPF3 activity weakens TM4SF1-AS1's drug response | lines that do not express DPF3 (11) vs lines expressing it (22) | the lines without DPF3 respond 1.86× as strongly (z diff -1.98); strongest at Homoharringtonine 5 µM: 0.27x vs 0.55x (z diff -4.7) | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DPF3]] | B | DPF3 activity lowers TM4SF1-AS1's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 1.98× higher at baseline in the lines without DPF3 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers TM4SF1-AS1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[NABP1]] | C | NABP1 activity raises TM4SF1-AS1's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without NABP1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NABP1]] | B | TM4SF1-AS1 activity raises NABP1's level | lines that do not express TM4SF1-AS1 (14) vs lines expressing it (36) | 1.65× lower at baseline in the lines without TM4SF1-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: CXCL1, MBP, TM4SF1 |
| [[ISG20]] | B | TM4SF1-AS1 activity raises ISG20's level | lines that do not express TM4SF1-AS1 (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without TM4SF1-AS1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CXCL1, MBP, TM4SF1 |
| [[TM4SF1]] | C | TM4SF1-AS1 activity raises TM4SF1's level | lines that do not express TM4SF1-AS1 (14) vs lines expressing it (36) | 3.43× lower at baseline in the lines without TM4SF1-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CXCL1, MBP, TM4SF1; co-absent with the target |
| [[CXCL1]] | C | TM4SF1-AS1 activity raises CXCL1's level | lines that do not express TM4SF1-AS1 (14) vs lines expressing it (36) | 2.70× lower at baseline in the lines without TM4SF1-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CXCL1, MBP, TM4SF1; co-absent with the target |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.0, 6.8); signed map (40.0, 2.8). **Vector** length 69.6, 14.2% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.3 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +4.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +3.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.0 | -12.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -1.9 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -8.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | TM4SF1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q25.1 — chr3:149,377,778-149,386,583 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40587) · Entrez [100874091](https://www.ncbi.nlm.nih.gov/gene/100874091) · Ensembl [ENSG00000240541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240541)

## Data

Gene col 14240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14240); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14240]; `tensor/DDL_lfc|DDL_z.npy` [14240]; `embed/gene_vectors.npy` [14240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14240 or target_col == 14240). Every well: [[TM4SF1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM4SF1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
