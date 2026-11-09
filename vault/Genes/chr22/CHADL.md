---
symbol: "CHADL"
type: "gene"
col: 1949
ensembl_id: "ENSG00000100399"
name: "chondroadherin like"
location: "22q13.2"
module: 47
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# CHADL

*chondroadherin like* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.94× (z +13.9, q 3e-41, up in 23 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.462× (z -5.6, q 1e-05, down in 21 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HEC-1-A 0.0663×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H2030 0.0421×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (Panc 03.27 0.0396×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPP4]] (+0.83, fdr 7e-06), [[L3MBTL2-AS1]] (+0.80, fdr 7e-06, ⚠ same locus), [[FNDC7]] (+0.80, fdr 7e-06), [[PILRA]] (+0.79, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.94×** | +13.9 | 3e-41 | 23/30 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.61×** | +13.0 | 2e-36 | 25/28 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +7.3 | 4e-11 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.57×** | +6.8 | 2e-09 | 20/35 (A-172, C32, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +5.6 | 2e-06 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.18×** | +5.6 | 2e-06 | 23/43 (NCI-H460, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +5.2 | 2e-05 | 2/9 (LoVo, NCI-H460) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +5.1 | 2e-05 | 10/21 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +4.9 | 7e-05 | 9/29 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.4 | 6e-04 | 10/42 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.79×** | +4.2 | 0.002 | 9/42 (SW480, A498, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.68×** | +3.7 | 0.010 | 4/45 (A498, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.67×** | +3.7 | 0.011 | 12/41 (A549, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.64×** | +3.5 | 0.016 | 11/41 (LoVo, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.5 | 0.017 | 2/16 (LOX-IMVI, SK-MEL-2) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.61×** | +3.1 | 0.056 | 2/17 (NCI-H1573, SW480) | inconsistent across doses | position effect removed |
| [[Rimonabant (drug)]] 5 µM |  | **1.34×** | +2.9 | 0.096 | 2/42 (SW480, KATO III) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +2.9 | 0.096 | 5/41 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1949.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HEC-1-A 0.0663×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H2030 0.0421×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (Panc 03.27 0.0396×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.462×** | -5.6 | 1e-05 | 21/43 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM |  | **0.674×** | -4.1 | 0.013 | 7/43 (C-33 A, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.640× | -3.3 | 0.16 | 17/39 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.640× | -3.3 | 0.16 | 11/18 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 2.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 7.33 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0663× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 0.927 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +8.9) | — |
| [[LoVo (line)]] | wt | 2.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 4.28 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0421× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 2.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0396× (z -8.5) |
| [[SW480 (line)]] | alt | 1.50 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0684× (z -8.5) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.575 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.744 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP4]] | +0.83 | +0.82 / +0.79 | both halves | 7e-06 |  |
| [[L3MBTL2-AS1]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 | ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[FNDC7]] | +0.80 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[PILRA]] | +0.79 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[KIF17]] | +0.78 | +0.79 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[MMP25]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.77 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.77 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.77 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.76 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.76 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.76 | +0.79 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CHADL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.866). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.9, -14.6); signed map (17.6, 12.2). **Vector** length 59.9, 8.91% of its response variance represented; |z| ≥ 3 in 1,193 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +3.4 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +0.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | chondroadherin like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,229,510-41,240,931 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLRR4B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUI6](https://www.uniprot.org/uniprotkb/Q6NUI6) (Chondroadherin-like protein):

> Potential negative modulator of chondrocyte differentiation. Inhibits collagen fibrillogenesis in vitro. May influence chondrocyte's differentiation by acting on its cellular collagenous microenvironment.

**Summary**, from NCBI Gene [150356](https://www.ncbi.nlm.nih.gov/gene/150356):

> Enables collagen binding activity and collagen fibril binding activity. Involved in negative regulation of collagen fibril organization. Is active in gel phase of interstitial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25165) · Entrez [150356](https://www.ncbi.nlm.nih.gov/gene/150356) · UniProt [Q6NUI6](https://www.uniprot.org/uniprotkb/Q6NUI6) · Ensembl [ENSG00000100399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100399)

## Data

Gene col 1949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1949); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1949]; `tensor/DDL_lfc|DDL_z.npy` [1949]; `embed/gene_vectors.npy` [1949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1949 or target_col == 1949). Every well: [[CHADL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHADL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
