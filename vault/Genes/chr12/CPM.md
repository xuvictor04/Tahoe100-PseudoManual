---
symbol: "CPM"
type: "gene"
col: 5740
ensembl_id: "ENSG00000135678"
name: "carboxypeptidase M"
location: "12q15"
module: 21
arm: "+"
pooled_cpm: 21.84
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CPM

*carboxypeptidase M* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.37× (z +20.0, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Clotrimazole (drug)]] 5 µM: 0.802× (z -4.2, q 0.014, down in 15 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCOA3]] (+0.58, fdr 3e-05), [[HSD11B1]] (+0.57, fdr 1e-05), [[PPP1R14C]] (+0.56, fdr 4e-05); moves opposite to [[PAAF1]] (-0.42, fdr 0.002, ⚠ not reproduced).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.37×** | +20.0 | 0e+00 | 40/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.80×** | +19.7 | 0e+00 | 42/47 (NCI-H460, A-427, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.53×** | +17.1 | 0e+00 | 40/46 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.49×** | +16.9 | 0e+00 | 39/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.92×** | +13.4 | 7e-39 | 19/29 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.65×** | +13.2 | 7e-38 | 24/34 (SW480, HOP62, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.47×** | +12.3 | 1e-32 | 33/47 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.44×** | +12.1 | 1e-31 | 33/45 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.24×** | +10.5 | 4e-24 | 20/25 (NCI-H460, HT-29, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.4 | 9e-12 | 25/45 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +6.1 | 5e-08 | 21/45 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.9 | 2e-07 | 16/47 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +5.1 | 2e-05 | 20/44 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +5.0 | 2e-05 | 17/45 (NCI-H460, LoVo, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.01×** | +4.9 | 3e-05 | 17/46 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.8 | 5e-05 | 14/46 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.6 | 1e-04 | 14/45 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 2e-04 | 13/46 (hTERT-HPNE, H4, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 3e-04 | 14/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clotrimazole (drug)]] 5 µM |  | **0.802×** | -4.2 | 0.014 | 15/48 (CFPAC-1, SNU-423, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -4.0 | 0.016 | 10/48 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.822×** | -3.7 | 0.035 | 17/47 (Panc 03.27, NCI-H2347, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -3.5 | 0.057 | 11/46 (AsPC-1, SHP-77, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.844× | -3.2 | 0.14 | 9/47 (NCI-H661, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.1 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 14.4× (z +16.6) | — |
| [[C32 (line)]] | wt | 23.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +16.5) | — |
| [[A-427 (line)]] | wt | 16.7 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 5.81× (z +14.3) | — |
| [[A549 (line)]] | wt | 33.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.24× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 5 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 16.7× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 24.0 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.53× (z +12.2) | — |
| [[A498 (line)]] | wt | 11.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.47× (z +10.2) | — |
| [[J82 (line)]] | alt | 25.1 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.55× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.19× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.15× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 27.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.91× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.50× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 11.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 11.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.20× (z +9.8) | — |
| [[LoVo (line)]] | wt | 16.0 | 2 | 0 | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM 4.25× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 6.83 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.04× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 56.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.32× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 8.48 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.48× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 8.56 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.27× (z +9.1) | — |
| [[KATO III (line)]] | alt | 8.66 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.27× (z +9.3) | — |
| [[SW480 (line)]] | alt | 6.80 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.83× (z +9.3) | — |
| [[A-172 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA3]] | +0.58 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[HSD11B1]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[PPP1R14C]] | +0.56 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[TGM2]] | +0.55 | +0.31 / +0.52 | both halves | 2e-04 |  |
| [[MTUS2]] | +0.55 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CYP2U1-AS1]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ATP6V1C2]] | +0.53 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[MFGE8]] | +0.52 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[LINC00540]] | +0.51 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CCDC69]] | +0.51 | +0.21 / +0.58 | both halves | 7e-04 |  |
| [[AMN1]] | +0.50 | +0.37 / +0.53 | both halves | 7e-05 |  |
| [[LINC02725]] | +0.50 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAAF1]] | -0.42 | -0.11 / -0.44 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CPM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.280). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.4, 14.5); signed map (12.3, 35.9). **Vector** length 85.7, 17.7% of its response variance represented; |z| ≥ 3 in 1,127 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.2 | +19.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.0 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +7.6 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +7.0 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | carboxypeptidase M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:68,842,197-68,971,570 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M14 carboxypeptidases |
| Hallmark sets | COMPLEMENT |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P14384](https://www.uniprot.org/uniprotkb/P14384) (Carboxypeptidase M):

> Specifically removes C-terminal basic residues (Arg or Lys) from peptides and proteins. It is believed to play important roles in the control of peptide hormone and growth factor activity at the cell surface, and in the membrane-localized degradation of extracellular proteins.

**Summary**, from NCBI Gene [1368](https://www.ncbi.nlm.nih.gov/gene/1368):

> The protein encoded by this gene is a membrane-bound arginine/lysine carboxypeptidase. Its expression is associated with monocyte to macrophage differentiation. This encoded protein contains hydrophobic regions at the amino and carboxy termini and has 6 potential asparagine-linked glycosylation sites. The active site residues of carboxypeptidases A and B are conserved in this protein. Three alternatively spliced transcript variants encoding the same protein have been described for this gene. …

**Accessions** — [HGNC:2311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2311) · Entrez [1368](https://www.ncbi.nlm.nih.gov/gene/1368) · UniProt [P14384](https://www.uniprot.org/uniprotkb/P14384) · Ensembl [ENSG00000135678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135678)

## Data

Gene col 5740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5740); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5740]; `tensor/DDL_lfc|DDL_z.npy` [5740]; `embed/gene_vectors.npy` [5740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5740 or target_col == 5740). Every well: [[CPM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
