---
symbol: "KRTAP5-AS1"
type: "gene"
col: 13932
ensembl_id: "ENSG00000233930"
name: "KRTAP5-1/KRTAP5-2 antisense RNA 1"
location: "11p15.5"
module: 123
arm: "+"
pooled_cpm: 6.04
n_lines_expressing: 38
n_dd_up: 57
n_dd_down: 4
n_dd_up_clean: 46
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# KRTAP5-AS1

*KRTAP5-1/KRTAP5-2 antisense RNA 1* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 57 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 13.2× (z +35.8, q 0e+00, up in 25 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.710× (z -4.8, q 8e-04, down in 16 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP8]] (+0.90, fdr 7e-06, ⚠ same locus), [[DUSP16]] (+0.68, fdr 7e-06), [[ELF3-AS1]] (+0.66, fdr 7e-06), [[JUND]] (+0.65, fdr 7e-06); moves opposite to [[SNHG30]] (-0.56, fdr 1e-05), [[METTL9]] (-0.55, fdr 2e-05), [[SHQ1]] (-0.55, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MISP]] → it (grade B ⚠); 4 go from it, the strongest it → [[DUSP8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 57 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **13.2×** | +35.8 | 0e+00 | 25/26 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **8.33×** | +20.0 | 0e+00 | 28/31 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.42×** | +14.6 | 0e+00 | 19/26 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **3.23×** | +11.0 | 4e-26 | 23/30 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.20×** | +10.5 | 6e-24 | 6/11 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **2.93×** | +10.5 | 6e-24 | 26/33 (COLO 205, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +10.4 | 1e-23 | 2/8 (NCI-H460, BT-474) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **2.10×** | +10.3 | 8e-23 | 26/32 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +9.5 | 2e-19 | 8/16 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **2.61×** | +9.4 | 4e-19 | 21/32 (NCI-H460, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **2.56×** | +9.2 | 2e-18 | 19/30 (COLO 205, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.23×** | +7.8 | 2e-13 | 16/33 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **2.21×** | +7.8 | 4e-13 | 20/28 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **2.19×** | +7.6 | 8e-13 | 18/32 (COLO 205, A-172, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **2.23×** | +7.5 | 2e-12 | 20/31 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.98×** | +7.1 | 4e-11 | 23/35 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +6.9 | 2e-10 | 10/32 (PANC-1, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.76×** | +6.6 | 1e-09 | 18/32 (NCI-H460, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.84×** | +6.2 | 1e-08 | 13/35 (NCI-H460, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +5.9 | 1e-07 | 11/30 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13932.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.710×** | -4.8 | 8e-04 | 16/35 (HT-29, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[NG25 (drug)]] 5 µM |  | **0.407×** | -4.6 | 9e-04 | 13/26 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.647×** | -4.3 | 0.003 | 10/32 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.679×** | -3.8 | 0.017 | 15/33 (RPMI-7951, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | 0.719× | -3.3 | 0.11 | 9/30 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 5 µM |  | 0.738× | -3.0 | 0.19 | 8/33 (NCI-H460, A549, …) | all doses, flat |  |
| [[Adenine (drug)]] 5 µM |  | 0.809× | -3.0 | 0.19 | 2/35 (SK-MEL-2, PANC-1) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 53.5 | 0 | 9 (9 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0784× (z -14.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 8.91 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +19.8) | [[Dexamethasone (drug)]] 0.5 µM 0.0881× (z -12.8) |
| [[LoVo (line)]] | wt | 21.8 | 2 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 6.21× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[NG25 (drug)]] 5 µM 0.0657× (z -9.8) |
| [[A-172 (line)]] | wt | 11.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +21.8) | — |
| [[A498 (line)]] | wt | 7.38 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +18.5) | — |
| [[NCI-H1573 (line)]] | alt | 4.26 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +13.3) | [[Raltitrexed (drug)]] 0.5 µM 0.0558× (z -9.1) |
| [[PANC-1 (line)]] | alt | 1.94 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 66.1× (z +19.0) | — |
| [[BT-474 (line)]] | alt | 32.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0708× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.0894× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 10.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +9.0) | [[Ponatinib (drug)]] 0.5 µM 0.0432× (z -10.5) |
| [[LS 180 (line)]] | wt | 14.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +13.0) | — |
| [[A549 (line)]] | wt | 4.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 6.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 1.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +9.0) | — |
| [[J82 (line)]] | alt | 1.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 99.0× (z +14.3) | — |
| [[KATO III (line)]] | alt | 6.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.66 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 14.6× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 2.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 4.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 2.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 5.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +15.5) | — |
| [[SW1417 (line)]] | alt | 4.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.80× (z +10.9) | — |
| [[SW48 (line)]] | wt | 4.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.6× (z +11.2) | — |
| [[SW480 (line)]] | alt | 1.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +10.9) | — |
| [[A-427 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP8]] | +0.90 | +0.87 / +0.92 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DUSP16]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[ELF3-AS1]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 | same gene group |
| [[JUND]] | +0.65 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[MMP25-AS1]] | +0.64 | +0.67 / +0.52 | both halves | 1e-05 | same gene group |
| [[ACHE]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[XKR4]] | +0.63 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[MAPK8IP2]] | +0.61 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[MVP-DT]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[KCNN1]] | +0.60 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[LINC00592]] | +0.60 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[LGALSL]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TP53INP2]] | +0.59 | +0.58 / +0.59 | both halves | 8e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG30]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[METTL9]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SHQ1]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[SKP2]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[TUFM]] | -0.53 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[INTS4]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[TTI1]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.52 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[EBPL]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ADPGK]] | -0.52 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[NFATC3]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[IPO11]] | -0.51 | -0.53 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MISP]] | B | MISP activity raises KRTAP5-AS1's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.20× lower at baseline in the lines without MISP | 0.030 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[KRT80]] | B | KRT80 activity raises KRTAP5-AS1's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without KRT80 | 0.039 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[MARCOL]] | B | MARCOL activity raises KRTAP5-AS1's level | lines that do not express MARCOL (45) vs lines expressing it (5) | 2.73× lower at baseline in the lines without MARCOL | 0.058 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975 |
| [[BTG3-AS1]] | B | BTG3-AS1 activity raises KRTAP5-AS1's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 2.28× lower at baseline in the lines without BTG3-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |
| [[NOXA1]] | B | NOXA1 activity raises KRTAP5-AS1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 2.28× lower at baseline in the lines without NOXA1 | 0.094 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[SRC]] | B | SRC activity raises KRTAP5-AS1's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[DNAJB5]] | C | DNAJB5 activity lowers KRTAP5-AS1's level | lines that do not express DNAJB5 (3) vs lines expressing it (47) | 4.11× higher at baseline in the lines without DNAJB5 | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: CEP170, SRGAP2C, TLCD5; maybe low, not absent |
| [[DUSP8]] | C | DUSP8 activity raises KRTAP5-AS1's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 2.91× lower at baseline in the lines without DUSP8 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP8]] | B | KRTAP5-AS1 activity raises DUSP8's level | lines that do not express KRTAP5-AS1 (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without KRTAP5-AS1 | 0.017 | ⚠ within organs, on part of the lines; also absent: LLGL2, TFR2, USP43; maybe low, not absent |
| [[ACHE]] | B | KRTAP5-AS1 activity raises ACHE's level | lines that do not express KRTAP5-AS1 (12) vs lines expressing it (38) | 1.73× lower at baseline in the lines without KRTAP5-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: LLGL2, TFR2, USP43; maybe low, not absent |
| [[TFE3]] | B | KRTAP5-AS1 activity raises TFE3's level | lines that do not express KRTAP5-AS1 (12) vs lines expressing it (38) | 1.28× lower at baseline in the lines without KRTAP5-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: LLGL2, TFR2, USP43; maybe low, not absent |
| [[USP43]] | C | KRTAP5-AS1 activity raises USP43's level | lines that do not express KRTAP5-AS1 (12) vs lines expressing it (38) | 3.28× lower at baseline in the lines without KRTAP5-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LLGL2, TFR2, USP43; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.6, 9.7); signed map (42.7, -3.6). **Vector** length 91.8, 21.2% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +35.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +20.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +6.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.7 | +7.6 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.2 | -4.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -4.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.4 | -4.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | KRTAP5-1/KRTAP5-2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p15.5 — chr11:1,571,353-1,599,184 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27877) · Entrez [338651](https://www.ncbi.nlm.nih.gov/gene/338651) · Ensembl [ENSG00000233930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233930)

## Data

Gene col 13932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13932); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13932]; `tensor/DDL_lfc|DDL_z.npy` [13932]; `embed/gene_vectors.npy` [13932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13932 or target_col == 13932). Every well: [[KRTAP5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRTAP5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
