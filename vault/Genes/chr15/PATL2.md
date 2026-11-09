---
symbol: "PATL2"
type: "gene"
col: 13706
ensembl_id: "ENSG00000229474"
name: "PAT1 homolog 2"
location: "15q21.1"
module: 68
arm: "+"
pooled_cpm: 6.62
n_lines_expressing: 49
n_dd_up: 41
n_dd_down: 4
n_dd_up_clean: 36
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# PATL2

*PAT1 homolog 2* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 21.8× (z +35.6, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.574× (z -4.5, q 0.003, down in 16 of 45 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAMP1-AS1]] (+0.84, fdr 7e-06), [[TAPBPL]] (+0.83, fdr 7e-06), [[RIPK2-DT]] (+0.83, fdr 7e-06); moves opposite to [[ANKRD27]] (-0.74, fdr 9e-05), [[WASF3]] (-0.72, fdr 4e-05), [[LPCAT4]] (-0.71, fdr 4e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **21.8×** | +35.6 | 0e+00 | 40/40 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **11.9×** | +20.2 | 0e+00 | 38/39 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.82×** | +18.1 | 0e+00 | 40/40 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **9.42×** | +17.6 | 0e+00 | 38/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.35×** | +9.9 | 6e-21 | 36/46 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +8.9 | 6e-17 | 28/37 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.62×** | +7.8 | 3e-13 | 30/45 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.85×** | +7.1 | 8e-11 | 25/45 (KATO III, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +6.7 | 1e-09 | 28/39 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.19×** | +6.4 | 9e-09 | 25/44 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.91×** | +5.3 | 7e-06 | 20/42 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +4.9 | 4e-05 | 4/15 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.64×** | +4.8 | 7e-05 | 18/44 (SK-MEL-2, LoVo, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.50×** | +4.6 | 2e-04 | 23/45 (LoVo, NCI-H23, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.73×** | +4.5 | 3e-04 | 20/46 (A498, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.001 | 19/42 (LoVo, SNU-423, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.001 | 15/46 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.002 | 14/46 (HepG2/C3A, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.574×** | -4.5 | 0.003 | 16/45 (COLO 205, C-33 A, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.583×** | -4.4 | 0.003 | 17/46 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[NG25 (drug)]] 5 µM |  | **0.391×** | -4.0 | 0.012 | 13/35 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.740×** | -3.5 | 0.071 | 15/46 (MIA PaCa-2, RKO, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.682× | -3.1 | 0.20 | 15/46 (C32, LoVo, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.682× | -3.0 | 0.24 | 10/46 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.2× (z +21.8) | — |
| [[COLO 205 (line)]] | alt | 40.4 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.57× (z +16.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -11.9) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.223× (z -8.6) |
| [[LoVo (line)]] | wt | 12.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.4× (z +24.4) | — |
| [[NCI-H460 (line)]] | wt | 8.33 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 172× (z +26.6) | — |
| [[PANC-1 (line)]] | alt | 4.92 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +18.2) | [[Digitoxin (drug)]] 5 µM 0.159× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 11.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +11.7) | [[Budesonide (drug)]] 0.5 µM 0.0617× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 8.19 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 7.30 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.6× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 2.55 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 87.6× (z +17.3) | — |
| [[J82 (line)]] | alt | 6.44 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.5× (z +18.9) | — |
| [[NCI-H1573 (line)]] | alt | 6.93 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +14.8) | — |
| [[NCI-H2347 (line)]] | alt | 2.51 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.5× (z +15.4) | — |
| [[SW 900 (line)]] | alt | 3.96 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.6× (z +14.7) | — |
| [[A498 (line)]] | wt | 4.93 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +11.9) | — |
| [[HCT15 (line)]] | alt | 6.20 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 78.8× (z +14.8) | — |
| [[HS-578T (line)]] | alt | 2.66 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 79.3× (z +15.1) | — |
| [[HT-29 (line)]] | alt | 6.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +14.6) | — |
| [[hTERT-HPNE (line)]] | wt | 4.40 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 167× (z +16.2) | — |
| [[KATO III (line)]] | alt | 18.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +16.9) | — |
| [[LOX-IMVI (line)]] | wt | 4.06 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.6× (z +15.8) | — |
| [[LS 180 (line)]] | wt | 3.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 90.0× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 4.29 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 125× (z +20.2) | — |
| [[Panc 03.27 (line)]] | alt | 4.48 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +13.4) | [[Vandetanib (drug)]] 0.05 µM 0.0647× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 17.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +16.7) | — |
| [[SNU-423 (line)]] | alt | 12.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +16.8) | — |
| [[SW48 (line)]] | wt | 5.47 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 84.8× (z +14.0) | — |
| [[SW480 (line)]] | alt | 2.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 2.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +8.9) | — |
| [[C32 (line)]] | wt | 5.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 5.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 62.8× (z +18.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.43 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0283× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 6.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +12.5) | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 4.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +8.6) | — |
| [[A-427 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 16 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAMP1-AS1]] | +0.84 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[TAPBPL]] | +0.83 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.83 | +0.87 / +0.62 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.82 | +0.86 / +0.43 | both halves | 3e-05 |  |
| [[TRIM69]] | +0.81 | +0.85 / +0.65 | both halves | 7e-06 | ⚠ same locus (17.7 kb: neighbours can correlate without regulation) |
| [[TMEM202-AS1]] | +0.80 | +0.87 / +0.32 | both halves | 2e-04 |  |
| [[GUCY2C-AS1]] | +0.80 | +0.85 / +0.48 | both halves | 2e-05 |  |
| [[LINC00240]] | +0.79 | +0.84 / +0.54 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.77 | +0.80 / +0.38 | both halves | 7e-05 |  |
| [[ZNF747]] | +0.77 | +0.76 / +0.44 | both halves | 3e-05 |  |
| [[WAC-AS1]] | +0.76 | +0.80 / +0.39 | both halves | 5e-05 |  |
| [[PPP1R12A-AS2]] | +0.76 | +0.82 / +0.23 | both halves | 5e-04 |  |
| [[MMADHC-DT]] | +0.76 | +0.80 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | -0.74 | -0.74 / -0.36 | both halves | 9e-05 |  |
| [[WASF3]] | -0.72 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[LPCAT4]] | -0.71 | -0.75 / -0.41 | both halves | 4e-05 |  |
| [[GNA12]] | -0.69 | -0.70 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PATL2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.0% of all compounds | 0.009 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises PATL2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SSPN]] | B | SSPN activity raises PATL2's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.32× lower at baseline in the lines without SSPN | 0.060 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[CTSO]] | B | CTSO activity raises PATL2's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without CTSO | 0.072 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[SPINK5]] | B | SPINK5 activity strengthens PATL2's drug response | lines that do not express SPINK5 (35) vs lines expressing it (12) | the lines without SPINK5 respond 0.75× as strongly (z diff +1.26); strongest at Harringtonine 5 µM: 7.85x vs 12x (z diff +2.0) | 0.076 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588; target measured in part of the lines; artifact flags |
| [[BTC]] | B | BTC activity raises PATL2's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.24× lower at baseline in the lines without BTC | 0.085 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[CLTCL1]] | C | CLTCL1 activity lowers PATL2's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 2.80× higher at baseline in the lines without CLTCL1 | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[DNAI4]] | C | DNAI4's natural level strengthens PATL2's drug response | DNAI4's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.16; direction not clear | 0.055 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[DPH6-DT]] | C | DPH6-DT activity raises PATL2's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without DPH6-DT | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.902). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.8, 12.3); signed map (23.0, -15.5). **Vector** length 115, 29.8% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.4 | +35.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.2 | +20.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.8 | +17.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.5 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +18.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.8 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.1 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.6 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.5 | -4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -0.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | PAT1 homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:44,665,732-44,711,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Pat1a |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [C9JE40](https://www.uniprot.org/uniprotkb/C9JE40) (Protein PAT1 homolog 2):

> RNA-binding protein that acts as a translational repressor.

**Summary**, from NCBI Gene [197135](https://www.ncbi.nlm.nih.gov/gene/197135):

> Predicted to enable RNA binding activity. Predicted to be involved in P-body assembly; deadenylation-dependent decapping of nuclear-transcribed mRNA; and negative regulation of translation. Predicted to act upstream of or within negative regulation of cytoplasmic mRNA processing body assembly. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33630](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33630) · Entrez [197135](https://www.ncbi.nlm.nih.gov/gene/197135) · UniProt [C9JE40](https://www.uniprot.org/uniprotkb/C9JE40) · Ensembl [ENSG00000229474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229474)

## Data

Gene col 13706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13706); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13706]; `tensor/DDL_lfc|DDL_z.npy` [13706]; `embed/gene_vectors.npy` [13706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13706 or target_col == 13706). Every well: [[PATL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PATL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
