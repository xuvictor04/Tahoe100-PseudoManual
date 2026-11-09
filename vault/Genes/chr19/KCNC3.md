---
symbol: "KCNC3"
type: "gene"
col: 5204
ensembl_id: "ENSG00000131398"
name: "potassium voltage-gated channel subfamily C member 3"
location: "19q13.33"
module: 17
arm: "-"
pooled_cpm: 11.71
n_lines_expressing: 41
n_dd_up: 15
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# KCNC3

*potassium voltage-gated channel subfamily C member 3* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.39× (z +14.2, q 1e-42, up in 31 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.628× (z -5.2, q 1e-04, down in 18 of 33 measured lines) ⚠ toxic. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.741× (z -4.9, q 2e-04, down in 20 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPYSL4]] (+0.57, fdr 1e-05), [[RELT]] (+0.52, fdr 4e-05), [[DBNL]] (+0.50, fdr 2e-05); moves opposite to [[APC]] (-0.56, fdr 1e-05), [[ZNF449]] (-0.47, fdr 5e-05), [[WDSUB1]] (-0.46, fdr 8e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EEF1A2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[EEF1A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.39×** | +14.2 | 1e-42 | 31/38 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.22×** | +13.6 | 2e-39 | 31/38 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +10.3 | 8e-23 | 26/38 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.77×** | +6.6 | 6e-09 | 20/38 (SW480, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.2 | 6e-08 | 21/37 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +6.0 | 2e-07 | 22/38 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.9 | 2e-07 | 18/39 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +5.8 | 5e-07 | 18/36 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +5.7 | 9e-07 | 20/38 (SW1417, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.1 | 2e-05 | 19/36 (PANC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.07×** | +4.4 | 5e-04 | 14/36 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 5e-04 | 19/36 (C-33 A, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.001 | 13/37 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.002 | 15/37 (NCI-H460, NCI-H2347, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +3.3 | 0.036 | 10/37 (SW1417, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5204.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.628×** | -5.2 | 1e-04 | 18/33 (SNU-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.652×** | -5.0 | 2e-04 | 19/37 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.741×** | -4.9 | 2e-04 | 20/38 (C32, PANC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.484×** | -4.4 | 0.002 | 13/21 (NCI-H2347, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.691×** | -4.3 | 0.002 | 17/37 (SW 900, C32, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -4.0 | 0.006 | 19/37 (A-427, C32, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.522×** | -3.9 | 0.007 | 15/34 (SHP-77, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.715×** | -3.9 | 0.007 | 13/38 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -3.9 | 0.007 | 15/37 (SW 900, A-427, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.734×** | -3.6 | 0.019 | 18/38 (NCI-H2030, NCI-H1792, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.739×** | -3.5 | 0.024 | 14/37 (COLO 205, NCI-H1573, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.725×** | -3.4 | 0.034 | 9/38 (SW 900, NCI-H23, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -3.4 | 0.034 | 8/37 (C32, HT-29, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.742×** | -3.3 | 0.036 | 9/38 (NCI-H23, Panc 03.27, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.749×** | -3.2 | 0.060 | 9/36 (SNU-423, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.84 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 12.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.8× (z +13.4) | — |
| [[SW480 (line)]] | alt | 6.80 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.74× (z +12.2) | — |
| [[A549 (line)]] | wt | 5.36 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 15.1× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 5.13 | 0 | 2 | — | [[Menadione (drug)]] 0.5 µM 0.0724× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 47.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -11.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.327× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 9.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -8.5) |
| [[LoVo (line)]] | wt | 5.67 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.53× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 7.91 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0708× (z -9.4) |
| [[SNU-423 (line)]] | alt | 5.18 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0573× (z -8.9) |
| [[A-172 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYSL4]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[RELT]] | +0.52 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[DBNL]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 | pathway: Neuronal System |
| [[CTXN1]] | +0.50 | +0.35 / +0.39 | both halves | 1e-04 |  |
| [[NLGN2]] | +0.49 | +0.49 / +0.39 | both halves | 5e-05 | pathway: Neuronal System |
| [[EPPK1]] | +0.47 | +0.50 / +0.37 | both halves | 9e-05 |  |
| [[FER1L4]] | +0.46 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[FGFRL1]] | +0.46 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[VGF]] | +0.45 | +0.40 / +0.39 | both halves | 6e-05 |  |
| [[TP53I11]] | +0.45 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[TUBB3]] | +0.45 | +0.44 / +0.40 | both halves | 5e-05 | pathway: Neuronal System |
| [[CSRNP1]] | +0.44 | +0.44 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APC]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ZNF449]] | -0.47 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[WDSUB1]] | -0.46 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[MTX2]] | -0.45 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[ESD]] | -0.45 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[MTO1]] | -0.44 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[MORN4]] | -0.44 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[FHIP2A]] | -0.44 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[NEK3]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SHPRH]] | -0.44 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[RWDD3]] | -0.44 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[LIAS]] | -0.43 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEF1A2]] | B | EEF1A2 activity raises KCNC3's level | lines that do not express EEF1A2 (11) vs lines expressing it (39) | 2.92× lower at baseline in the lines without EEF1A2 | 0.037 | ⚠ within organs, on part of the lines; also absent: NRG2, RRAGD, RAB39A |
| [[TOP2A]] | B | TOP2A activity lowers KCNC3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEF1A2]] | B | KCNC3 activity raises EEF1A2's level | lines that do not express KCNC3 (9) vs lines expressing it (41) | 2.68× lower at baseline in the lines without KCNC3 | 0.064 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.327). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.7, 15.8); signed map (1.2, 20.9). **Vector** length 71.9, 14.4% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.0 | +1.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.9 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +5.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +5.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily C member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:50,311,937-50,333,515 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kv3.3; previously SCA13 |
| Gene groups (HGNC) | Potassium voltage-gated channels; BTB domain containing |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14003](https://www.uniprot.org/uniprotkb/Q14003) (Voltage-gated potassium channel KCNC3):

> Voltage-gated potassium channel that plays an important role in the rapid repolarization of fast-firing brain neurons. The channel opens in response to the voltage difference across the membrane, forming a potassium-selective channel through which potassium ions pass in accordance with their electrochemical gradient. The channel displays rapid activation and inactivation kinetics. It plays a role in the regulation of the frequency, shape and duration of action potentials in Purkinje cells. …

**Summary**, from NCBI Gene [3748](https://www.ncbi.nlm.nih.gov/gene/3748):

> The Shaker gene family of Drosophila encodes components of voltage-gated potassium channels and is comprised of four subfamilies. Based on sequence similarity, this gene is similar to one of these subfamilies, namely the Shaw subfamily. The protein encoded by this gene belongs to the delayed rectifier class of channel proteins and is an integral membrane protein that mediates the voltage-dependent potassium ion permeability of excitable membranes. Alternate splicing results in several …

**Accessions** — [HGNC:6235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6235) · Entrez [3748](https://www.ncbi.nlm.nih.gov/gene/3748) · UniProt [Q14003](https://www.uniprot.org/uniprotkb/Q14003) · Ensembl [ENSG00000131398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131398)

## Data

Gene col 5204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5204); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5204]; `tensor/DDL_lfc|DDL_z.npy` [5204]; `embed/gene_vectors.npy` [5204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5204 or target_col == 5204). Every well: [[KCNC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
