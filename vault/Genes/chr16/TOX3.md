---
symbol: "TOX3"
type: "gene"
col: 2368
ensembl_id: "ENSG00000103460"
name: "TOX high mobility group box family member 3"
location: "16q12.1"
module: 8
arm: "+"
pooled_cpm: 32.53
n_lines_expressing: 19
n_dd_up: 24
n_dd_down: 13
n_dd_up_clean: 18
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 130
direction_downstream: 173
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TOX3

*TOX high mobility group box family member 3* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.73× (z +6.7, q 1e-08, up in 0 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +5.9, q 6e-07, up in 7 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.463× (z -9.3, q 7e-18, down in 14 of 17 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.686× (z -4.5, q 6e-04, down in 13 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POF1B]] (+0.84, fdr 7e-06), [[TMPRSS2]] (+0.79, fdr 7e-06), [[RNF43]] (+0.79, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 130 arrows point to it, the strongest [[LDLRAD4]] → it (grade B ⚠); 173 go from it, the strongest it → [[ELF3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.7 | 1e-08 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +6.5 | 2e-08 | 1/12 (A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +5.9 | 6e-07 | 7/17 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +5.4 | 1e-05 | 2/15 (NCI-H1573, A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.42×** | +4.3 | 0.002 | 8/17 (SW1417, NCI-H1573, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +4.2 | 0.002 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.003 | 1/17 (A549) | rises with dose | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.0 | 0.004 | 7/17 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.006 | 7/17 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.009 | 0/17 | rises with dose |  |
| [[Alpelisib (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.015 | 4/17 (AsPC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.033 | 0/17 | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.69×** | +3.3 | 0.036 | 5/17 (AsPC-1, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **1.67×** | +3.3 | 0.043 | 6/17 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.043 | 0/17 | rises with dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.045 | 3/17 (SHP-77, COLO 205, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.053 | 9/17 (AsPC-1, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.056 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.071 | 2/17 (AsPC-1, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.071 | 1/17 (KATO III) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.071 | 8/17 (AsPC-1, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.463×** | -9.3 | 7e-18 | 14/17 (SW480, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.545×** | -7.3 | 6e-11 | 15/17 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.561×** | -7.0 | 5e-10 | 14/17 (SW480, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.605×** | -6.1 | 2e-07 | 10/17 (KATO III, COLO 205, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.686×** | -4.5 | 6e-04 | 13/17 (COLO 205, SW480, …) | two highest doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.679×** | -4.3 | 0.001 | 0/17 | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 5 µM |  | **0.705×** | -4.0 | 0.004 | 1/17 (A549) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.701×** | -4.0 | 0.005 | 0/17 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.730×** | -3.8 | 0.009 | 11/17 (COLO 205, LS 180, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.743×** | -3.6 | 0.020 | 4/17 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.668×** | -3.5 | 0.026 | 0/17 | inconsistent across doses | noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.733×** | -3.5 | 0.026 | 0/17 | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.690×** | -3.2 | 0.061 | 2/17 (KATO III, LoVo) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.778× | -3.0 | 0.11 | 11/17 (COLO 205, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.60 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 267 | 0 | 15 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.235× (z -9.9) |
| [[LoVo (line)]] | wt | 112 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -19.4) ⚠ cell-cycle shift, explains ~60% of this change |
| [[LS 180 (line)]] | wt | 60.1 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -14.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 123 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0552× (z -22.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HT-29 (line)]] | alt | 129 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0684× (z -17.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 136 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -15.9) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SHP-77 (line)]] | alt | 134 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0671× (z -21.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 77.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -11.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -11.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.260× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POF1B]] | +0.84 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RNF43]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RASSF6]] | +0.77 | +0.68 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ARHGEF38]] | +0.77 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC02253]] | +0.77 | +0.62 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.76 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[PIP5K1B]] | +0.74 | +0.76 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[AXIN2]] | +0.74 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ERBB3]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.74 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[PROM1]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*130 arrows, 130 of them with an alert ⚠; grade A 0, B 10, C 120. Shown: the 12 strongest; 118 more arrows (118 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDLRAD4]] | B | LDLRAD4 activity raises TOX3's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 2.39× lower at baseline in the lines without LDLRAD4 | 0.020 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises TOX3's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.85× lower at baseline in the lines without ELF3-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[ZNF703]] | B | ZNF703 activity raises TOX3's level | lines that do not express ZNF703 (12) vs lines expressing it (38) | 3.34× lower at baseline in the lines without ZNF703 | 0.045 | ⚠ within organs, on part of the lines; also absent: HOXA10; maybe low, not absent |
| [[HNF4G]] | B | HNF4G activity raises TOX3's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.63× lower at baseline in the lines without HNF4G | 0.048 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[SPATA6L]] | B | SPATA6L activity raises TOX3's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.65× lower at baseline in the lines without SPATA6L | 0.056 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises TOX3's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.30× lower at baseline in the lines without SLC44A3-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[PELI2]] | B | PELI2 activity raises TOX3's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without PELI2 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[STS]] | B | STS activity raises TOX3's level | lines that do not express STS (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without STS | 0.079 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[KIRREL1]] | B | KIRREL1 activity lowers TOX3's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 8.08× higher at baseline in the lines without KIRREL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[SLC44A3]] | B | SLC44A3 activity raises TOX3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.21× lower at baseline in the lines without SLC44A3 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[TFF3]] | C | TFF3 activity raises TOX3's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 14.36× lower at baseline in the lines without TFF3 | 5e-05 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises TOX3's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 10.13× lower at baseline in the lines without TMEM45B | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |

### Downstream of this gene

*173 arrows, 173 of them with an alert ⚠; grade A 0, B 46, C 127. Shown: the 12 strongest; 161 more arrows (161 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | TOX3 activity raises ELF3-AS1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 4.15× lower at baseline in the lines without TOX3 | 8e-05 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[TNFRSF21]] | B | TOX3 activity raises TNFRSF21's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 4.84× lower at baseline in the lines without TOX3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[GAREM1]] | B | TOX3 activity raises GAREM1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.54× lower at baseline in the lines without TOX3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[SLC44A3-AS1]] | B | TOX3 activity raises SLC44A3-AS1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.39× lower at baseline in the lines without TOX3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[SLC37A1]] | B | TOX3 activity raises SLC37A1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.95× lower at baseline in the lines without TOX3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[SLC44A3]] | B | TOX3 activity raises SLC44A3's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.93× lower at baseline in the lines without TOX3 | 0.001 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[ZNF703]] | B | TOX3 activity raises ZNF703's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.96× lower at baseline in the lines without TOX3 | 0.001 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[NUDT4]] | B | TOX3 activity raises NUDT4's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without TOX3 | 0.003 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[PELI2]] | B | TOX3 activity raises PELI2's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.88× lower at baseline in the lines without TOX3 | 0.003 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[PLEKHA7]] | B | TOX3 activity raises PLEKHA7's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.80× lower at baseline in the lines without TOX3 | 0.005 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[TMEM184A]] | B | TOX3 activity raises TMEM184A's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.43× lower at baseline in the lines without TOX3 | 0.005 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[MFSD6]] | B | TOX3 activity raises MFSD6's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without TOX3 | 0.005 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.5, 50.4); signed map (58.4, 4.0). **Vector** length 82.0, 33.6% of its response variance represented; |z| ≥ 3 in 466 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.0 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | -1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +3.0 |
| fall | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.9 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TOX high mobility group box family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:52,436,417-52,547,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAGF9; previously TNRC9 |
| Gene groups (HGNC) | thymocyte selection associated high mobility group box family |
| Matched by | ensembl_id |

**Function**, from UniProt [O15405](https://www.uniprot.org/uniprotkb/O15405) (TOX high mobility group box family member 3):

> Transcriptional coactivator of the p300/CBP-mediated transcription complex. Activates transactivation through cAMP response element (CRE) sites. Protects against cell death by inducing antiapoptotic and repressing pro-apoptotic transcripts. Stimulates transcription from the estrogen-responsive or BCL-2 promoters. Required for depolarization-induced transcription activation of the C-FOS promoter in neurons. Associates with chromatin to the estrogen-responsive C3 promoter region.

**Summary**, from NCBI Gene [27324](https://www.ncbi.nlm.nih.gov/gene/27324):

> The protein encoded by this gene contains an HMG-box, indicating that it may be involved in bending and unwinding of DNA and alteration of chromatin structure. The C-terminus of the encoded protein is glutamine-rich due to CAG repeats in the coding sequence. A minor allele of this gene has been implicated in an elevated risk of breast cancer. Two transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:11972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11972) · Entrez [27324](https://www.ncbi.nlm.nih.gov/gene/27324) · UniProt [O15405](https://www.uniprot.org/uniprotkb/O15405) · Ensembl [ENSG00000103460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103460)

## Data

Gene col 2368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2368); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2368]; `tensor/DDL_lfc|DDL_z.npy` [2368]; `embed/gene_vectors.npy` [2368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2368 or target_col == 2368). Every well: [[TOX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
