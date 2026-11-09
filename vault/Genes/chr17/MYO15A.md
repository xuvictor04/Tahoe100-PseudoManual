---
symbol: "MYO15A"
type: "gene"
col: 1668
ensembl_id: "ENSG00000091536"
name: "myosin XVA"
location: "17p11.2"
module: 47
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# MYO15A

*myosin XVA* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.39× (z +11.1, q 9e-26, up in 19 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.559× (z -5.2, q 9e-05, down in 17 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPX]] (+0.78, fdr 7e-06), [[TINCR]] (+0.77, fdr 7e-06), [[RFPL3S]] (+0.77, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ASGR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.39×** | +11.1 | 9e-26 | 19/34 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.05×** | +10.0 | 3e-21 | 34/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +9.5 | 4e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +7.9 | 4e-13 | 28/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +7.3 | 4e-11 | 7/11 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.18×** | +7.0 | 2e-10 | 16/37 (LoVo, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.0 | 3e-10 | 15/30 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +6.4 | 8e-09 | 15/44 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +5.9 | 2e-07 | 16/44 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +5.4 | 5e-06 | 16/44 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +4.8 | 8e-05 | 10/28 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +3.9 | 0.005 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.59×** | +3.8 | 0.005 | 7/26 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.2 | 0.052 | 1/12 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.053 | 3/42 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.95×** | +3.1 | 0.061 | 0/15 | top dose only | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.072 | 5/43 (A549, LOX-IMVI, …) | two highest doses |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.085 | 3/23 (HCT15, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1668.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.559×** | -5.2 | 9e-05 | 17/46 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.584×** | -4.9 | 3e-04 | 16/42 (NCI-H1573, J82, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM |  | **0.657×** | -3.8 | 0.022 | 9/32 (SHP-77, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.657×** | -3.8 | 0.022 | 16/38 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.689×** | -3.4 | 0.087 | 11/18 (PANC-1, SW480, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.501× | -3.3 | 0.11 | 4/24 (Panc 03.27, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.779× | -3.2 | 0.12 | 13/42 (LS 180, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.707× | -3.1 | 0.12 | 7/45 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.66 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +10.9) | [[Sulfatinib (drug)]] 0.05 µM 0.0860× (z -8.5) |
| [[LoVo (line)]] | wt | 2.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.20× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 6.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +9.4) | — |
| [[A-172 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.908 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.738 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.799 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.803 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPX]] | +0.78 | +0.77 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TINCR]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[PTCH2]] | +0.76 | +0.78 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CPNE9]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.75 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[PILRA]] | +0.75 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.74 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[SGSM3-AS1]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[KIF17]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[MASP2]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASGR1]] | B | ASGR1 activity raises MYO15A's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without ASGR1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises MYO15A's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without LINC00334 | 0.037 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[RUNDC3A-AS1]] | B | RUNDC3A-AS1 activity raises MYO15A's level | lines that do not express RUNDC3A-AS1 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without RUNDC3A-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ERO1B, TEX14, TCTN1; maybe low, not absent; its own permutation p |
| [[HCN2]] | B | HCN2 activity raises MYO15A's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 1.58× lower at baseline in the lines without HCN2 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent |
| [[LINC01250]] | B | LINC01250 activity strengthens MYO15A's drug response | lines that do not express LINC01250 (10) vs lines expressing it (35) | the lines without LINC01250 respond 0.52× as strongly (z diff +1.19); strongest at Homoharringtonine 5 µM: 1.16x vs 2.43x (z diff +2.6) | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SSC5D]] | B | SSC5D activity raises MYO15A's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without SSC5D | 0.097 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[NECAB2]] | C | NECAB2 activity raises MYO15A's level | lines that do not express NECAB2 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without NECAB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, PARP11, DLG4; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.9, -18.0); signed map (14.9, 13.1). **Vector** length 51.7, 6.66% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +7.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +6.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.6 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | myosin XVA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,108,756-18,179,802 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DFNB3, MYO15 |
| Gene groups (HGNC) | Myosin heavy chains, class XV; FERM domain containing; SH3 domain containing |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKN7](https://www.uniprot.org/uniprotkb/Q9UKN7) (Unconventional myosin-XV):

> Myosins are actin-based motor molecules with ATPase activity. Unconventional myosins serve in intracellular movements. Their highly divergent tails are presumed to bind to membranous compartments, which would be moved relative to actin filaments. Required for the arrangement of stereocilia in mature hair bundles (By similarity).

**Summary**, from NCBI Gene [51168](https://www.ncbi.nlm.nih.gov/gene/51168):

> This gene encodes an unconventional myosin. This protein differs from other myosins in that it has a long N-terminal extension preceding the conserved motor domain. Studies in mice suggest that this protein is necessary for actin organization in the hair cells of the cochlea. Mutations in this gene have been associated with profound, congenital, neurosensory, nonsyndromal deafness. This gene is located within the Smith-Magenis syndrome region on chromosome 17. Read-through transcripts …

**Accessions** — [HGNC:7594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7594) · Entrez [51168](https://www.ncbi.nlm.nih.gov/gene/51168) · UniProt [Q9UKN7](https://www.uniprot.org/uniprotkb/Q9UKN7) · Ensembl [ENSG00000091536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091536)

## Data

Gene col 1668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1668); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1668]; `tensor/DDL_lfc|DDL_z.npy` [1668]; `embed/gene_vectors.npy` [1668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1668 or target_col == 1668). Every well: [[MYO15A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO15A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
