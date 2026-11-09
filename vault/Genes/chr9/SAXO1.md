---
symbol: "SAXO1"
type: "gene"
col: 7926
ensembl_id: "ENSG00000155875"
name: "stabilizer of axonemal microtubules 1"
location: "9p22.1"
module: 26
arm: "+"
pooled_cpm: 2.09
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SAXO1

*stabilizer of axonemal microtubules 1* — 9p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 16.9× (z +35.7, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.507× (z -6.0, q 8e-07, down in 21 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIAH2-AS1]] (+0.82, fdr 7e-06), [[PSMD7-DT]] (+0.81, fdr 7e-06), [[PELO-AS1]] (+0.77, fdr 7e-06); moves opposite to [[COMMD2]] (-0.66, fdr 3e-05), [[MRPS31P4]] (-0.65, fdr 3e-05), [[TTC26]] (-0.64, fdr 2e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **16.9×** | +35.7 | 0e+00 | 32/32 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.21×** | +15.7 | 0e+00 | 27/32 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.69×** | +14.9 | 0e+00 | 19/27 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.34×** | +10.7 | 9e-25 | 19/44 (HOP62, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **3.26×** | +10.6 | 6e-24 | 25/40 (SW480, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +9.3 | 1e-18 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +7.3 | 3e-11 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +5.8 | 5e-07 | 3/11 (SW 900, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +5.6 | 1e-06 | 13/35 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +4.4 | 6e-04 | 9/45 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +4.3 | 8e-04 | 7/43 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +4.2 | 0.001 | 14/44 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.003 | 7/41 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.004 | 5/26 (SW 900, A-427, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.008 | 8/44 (A549, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.023 | 5/37 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.47×** | +3.2 | 0.044 | 2/34 (NCI-H23, NCI-H460) | inconsistent across doses |  |
| [[Monocrotaline (drug)]] 0.05 µM |  | **1.45×** | +3.1 | 0.060 | 0/24 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7926.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.507×** | -6.0 | 8e-07 | 21/45 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -5.0 | 2e-04 | 13/40 (NCI-H23, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.591×** | -4.7 | 5e-04 | 12/43 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.612×** | -4.2 | 0.004 | 12/39 (J82, A-172, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.670×** | -3.6 | 0.041 | 6/45 (A549, A498, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.509× | -3.1 | 0.15 | 3/25 (A498, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1.62 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.1× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 2.20 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.2× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 3.34 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +9.1) | [[Erythromycin (drug)]] 0.5 µM 0.0768× (z -8.7) |
| [[A-172 (line)]] | wt | 1.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.9× (z +11.3) | — |
| [[A498 (line)]] | wt | 3.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +12.1) | — |
| [[A549 (line)]] | wt | 1.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +9.3) | — |
| [[C32 (line)]] | wt | 3.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 1.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.3× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 3.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.97× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 2.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.1× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 1.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.2× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 2.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +8.7) | — |
| [[KATO III (line)]] | alt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +9.7) | — |
| [[LoVo (line)]] | wt | 1.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 3.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.7× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 1.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 4.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.95× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 1.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.1× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 1.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.6× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 3.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.3× (z +9.4) | — |
| [[A-427 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.634 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.682 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.951 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIAH2-AS1]] | +0.82 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.81 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[PELO-AS1]] | +0.77 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.77 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[MYLK4]] | +0.76 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LINC00393]] | +0.76 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[CIBAR1-DT]] | +0.76 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.75 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.74 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ALG1L9P]] | +0.73 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[C2orf88]] | +0.73 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[LINC01762]] | +0.72 | +0.64 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.66 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[MRPS31P4]] | -0.65 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[TTC26]] | -0.64 | -0.31 / -0.56 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SAXO1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYOM1]] | B | MYOM1 activity raises SAXO1's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.21× lower at baseline in the lines without MYOM1 | 0.042 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC01762]] | B | LINC01762 activity raises SAXO1's level | lines that do not express LINC01762 (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without LINC01762 | 0.043 | ⚠ within organs, on part of the lines; also absent: MPP4, LINC01429, DNAH6; maybe low, not absent |
| [[CFAP58]] | B | CFAP58 activity raises SAXO1's level | lines that do not express CFAP58 (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CFAP58 | 0.094 | ⚠ within organs, on part of the lines; also absent: MINDY4, ENSG00000286162, MPP4; maybe low, not absent |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises SAXO1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[LRRIQ3]] | C | LRRIQ3 activity raises SAXO1's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.33× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.790). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.3, 18.8); signed map (25.4, -1.9). **Vector** length 56.2, 7.55% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +35.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +10.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.8 | +4.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.8 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.6 | -4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | stabilizer of axonemal microtubules 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.1 — chr9:18,858,906-19,049,358 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35182; previously C9orf138, FAM154A |
| Gene groups (HGNC) | Stabilizer of axonemal microtubules family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYX7](https://www.uniprot.org/uniprotkb/Q8IYX7) (Stabilizer of axonemal microtubules 1):

> May play a role in the regulation of cilium length. Stabilizes microtubules at low temperature.

**Summary**, from NCBI Gene [158297](https://www.ncbi.nlm.nih.gov/gene/158297):

> Enables microtubule binding activity. Involved in several processes, including cold acclimation; positive regulation of cilium assembly; and protein stabilization. Located in microtubule cytoskeleton and sperm flagellum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28566) · Entrez [158297](https://www.ncbi.nlm.nih.gov/gene/158297) · UniProt [Q8IYX7](https://www.uniprot.org/uniprotkb/Q8IYX7) · Ensembl [ENSG00000155875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155875)

## Data

Gene col 7926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7926); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7926]; `tensor/DDL_lfc|DDL_z.npy` [7926]; `embed/gene_vectors.npy` [7926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7926 or target_col == 7926). Every well: [[SAXO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAXO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
