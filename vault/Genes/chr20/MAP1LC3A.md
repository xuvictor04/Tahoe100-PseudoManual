---
symbol: "MAP1LC3A"
type: "gene"
col: 2143
ensembl_id: "ENSG00000101460"
name: "microtubule associated protein 1 light chain 3 alpha"
location: "20q11.22"
module: 39
arm: "+"
pooled_cpm: 7.42
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 5
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# MAP1LC3A

*microtubule associated protein 1 light chain 3 alpha* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.78× (z +11.0, q 2e-25, up in 11 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +8.9, q 1e-16, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.562× (z -6.5, q 5e-08, down in 22 of 43 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.677× (z -4.4, q 0.003, down in 16 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE9]] (+0.61, fdr 7e-06), [[SGSM3-AS1]] (+0.60, fdr 1e-05), [[MFSD2B]] (+0.60, fdr 7e-06); moves opposite to [[RPE]] (-0.51, fdr 3e-05), [[HAUS6]] (-0.48, fdr 8e-05), [[HEATR3]] (-0.48, fdr 4e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 5 go from it, the strongest it → [[GP6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +11.0 | 2e-25 | 11/15 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +9.1 | 2e-17 | 16/24 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +8.9 | 1e-16 | 24/38 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +8.0 | 1e-13 | 7/20 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +7.6 | 2e-12 | 25/38 (BT-474, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +7.6 | 2e-12 | 24/43 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +7.5 | 7e-12 | 26/44 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +7.2 | 5e-11 | 20/43 (BT-474, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.1 | 2e-05 | 14/33 (Panc 03.27, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.002 | 9/42 (A-172, PANC-1, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.003 | 12/39 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.023 | 9/44 (HepG2/C3A, J82, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.025 | 9/32 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.034 | 11/41 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.094 | 10/42 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.562×** | -6.5 | 5e-08 | 22/43 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -4.4 | 0.003 | 16/41 (LS 180, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | **0.781×** | -3.9 | 0.015 | 13/44 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.723×** | -3.7 | 0.037 | 6/43 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.743×** | -3.4 | 0.085 | 10/41 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.569×** | -3.3 | 0.085 | 10/39 (SW1417, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.666×** | -3.3 | 0.089 | 9/44 (MIA PaCa-2, SW 1088, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.742× | -3.2 | 0.10 | 12/41 (NCI-H1792, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.140× (z -9.2) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 3.02 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0595× (z -8.6) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0956× (z -9.5) |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0536× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 4.39 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0628× (z -10.0) |
| [[LoVo (line)]] | wt | 3.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.4) |
| [[A-172 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE9]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SGSM3-AS1]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MFSD2B]] | +0.60 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[USP50]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SELPLG]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[RAB11FIP4]] | +0.58 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[AVIL]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TEX29]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[OIT3]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SLC5A11]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ROPN1L]] | +0.56 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[HCLS1]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPE]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[HAUS6]] | -0.48 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[HEATR3]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[PRKDC]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GP6]] | C | MAP1LC3A activity lowers GP6's level | lines that do not express MAP1LC3A (4) vs lines expressing it (46) | 1.57× higher at baseline in the lines without MAP1LC3A | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285155; maybe low, not absent; its own permutation p |
| [[LINC00672]] | C | MAP1LC3A activity raises LINC00672's level | lines that do not express MAP1LC3A (4) vs lines expressing it (46) | 1.56× lower at baseline in the lines without MAP1LC3A | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285155; maybe low, not absent; its own permutation p |
| [[SPATA21]] | C | MAP1LC3A activity lowers SPATA21's level | lines that do not express MAP1LC3A (4) vs lines expressing it (46) | 1.06× higher at baseline in the lines without MAP1LC3A | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285155; maybe low, not absent; its own permutation p |
| [[AVIL]] | C | MAP1LC3A activity raises AVIL's level | lines that do not express MAP1LC3A (4) vs lines expressing it (46) | 2.46× lower at baseline in the lines without MAP1LC3A | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285155; maybe low, not absent |
| [[LPAR5]] | C | MAP1LC3A activity raises LPAR5's level | lines that do not express MAP1LC3A (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without MAP1LC3A | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285155; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.2, -13.6); signed map (18.9, 10.4). **Vector** length 58.3, 8.60% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +8.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +9.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.9 | +4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 1 light chain 3 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,546,854-34,560,345 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAP1BLC3, MAP1ALC3, LC3, LC3A, ATG8E |
| Gene groups (HGNC) | Autophagy related; Microtubule associated protein 1 light chain 3 family |
| Reactome | 6 pathways, smallest: Receptor Mediated Mitophagy; PINK1-PRKN Mediated Mitophagy; Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H492](https://www.uniprot.org/uniprotkb/Q9H492) (Microtubule-associated protein 1 light chain 3 alpha):

> Ubiquitin-like modifier involved in formation of autophagosomal vacuoles (autophagosomes). While LC3s are involved in elongation of the phagophore membrane, the GABARAP/GATE-16 subfamily is essential for a later stage in autophagosome maturation. Through its interaction with the reticulophagy receptor TEX264, participates in the remodeling of subdomains of the endoplasmic reticulum into autophagosomes upon nutrient stress, which then fuse with lysosomes for endoplasmic reticulum turnover.

**Summary**, from NCBI Gene [84557](https://www.ncbi.nlm.nih.gov/gene/84557):

> MAP1A and MAP1B are microtubule-associated proteins which mediate the physical interactions between microtubules and components of the cytoskeleton. MAP1A and MAP1B each consist of a heavy chain subunit and multiple light chain subunits. The protein encoded by this gene is one of the light chain subunits and can associate with either MAP1A or MAP1B. Two transcript variants encoding different isoforms have been found for this gene. The expression of variant 1 is suppressed in many tumor cell …

**Accessions** — [HGNC:6838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6838) · Entrez [84557](https://www.ncbi.nlm.nih.gov/gene/84557) · UniProt [Q9H492](https://www.uniprot.org/uniprotkb/Q9H492) · Ensembl [ENSG00000101460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101460)

## Data

Gene col 2143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2143); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2143]; `tensor/DDL_lfc|DDL_z.npy` [2143]; `embed/gene_vectors.npy` [2143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2143 or target_col == 2143). Every well: [[MAP1LC3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP1LC3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
