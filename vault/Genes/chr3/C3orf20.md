---
symbol: "C3orf20"
type: "gene"
col: 5201
ensembl_id: "ENSG00000131379"
name: "family with sequence similarity 194 member C"
location: "3p25.1"
module: 39
arm: "+"
pooled_cpm: 6.88
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# C3orf20

*family with sequence similarity 194 member C* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.28× (z +23.2, q 0e+00, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.513× (z -6.0, q 6e-07, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC22A1]] (+0.86, fdr 7e-06), [[USP50]] (+0.85, fdr 7e-06), [[MYOCOS]] (+0.84, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PXMP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.28×** | +23.2 | 0e+00 | 39/40 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.57×** | +15.3 | 0e+00 | 39/40 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.33×** | +10.3 | 2e-22 | 39/45 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +10.0 | 3e-21 | 33/42 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +6.3 | 3e-08 | 6/12 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +5.6 | 2e-06 | 23/45 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +5.5 | 3e-06 | 20/47 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +4.7 | 2e-04 | 6/19 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.007 | 10/46 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.57×** | +3.8 | 0.009 | 13/45 (Panc 03.27, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +3.7 | 0.009 | 17/44 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.012 | 14/47 (HepG2/C3A, C-33 A, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.06×** | +3.4 | 0.034 | 5/45 (LoVo, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.047 | 13/46 (LoVo, HCT15, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +3.1 | 0.063 | 9/46 (NCI-H2030, RPMI-7951, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.085 | 2/46 (RPMI-7951, hTERT-HPNE) | rises with dose |  |
| [[Lucanthone (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.086 | 7/46 (AsPC-1, A549, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.90×** | +3.0 | 0.092 | 3/39 (LoVo, RKO, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5201.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -6.0 | 6e-07 | 25/46 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.515×** | -6.0 | 6e-07 | 25/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.520×** | -5.9 | 7e-07 | 24/42 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.549×** | -5.4 | 9e-06 | 24/45 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[NG25 (drug)]] 5 µM |  | **0.332×** | -5.2 | 3e-05 | 22/37 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.673×** | -5.1 | 3e-05 | 23/46 (RKO, J82, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.634×** | -3.9 | 0.008 | 14/43 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.698×** | -3.3 | 0.079 | 14/46 (Panc 03.27, SNU-423, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 0.711× | -3.1 | 0.12 | 12/42 (LOX-IMVI, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.713× | -3.1 | 0.12 | 14/44 (NCI-H460, NCI-H661, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.98 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +13.2) | [[Pioglitazone (drug)]] 0.05 µM 0.0763× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 8.35 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.74× (z +12.3) | [[Digitoxin (drug)]] 5 µM 0.0534× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0559× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 3.15 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +17.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 13.3 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.0996× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0976× (z -9.0) |
| [[C32 (line)]] | wt | 5.75 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +9.9) | [[Gallic acid (drug)]] 0.05 µM 0.0458× (z -8.7) |
| [[LoVo (line)]] | wt | 26.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +15.2) | — |
| [[C-33 A (line)]] | alt | 12.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +9.3) | [[Decitabine (drug)]] 5 µM 0.0866× (z -8.8) |
| [[HOP62 (line)]] | alt | 4.47 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +14.6) | — |
| [[J82 (line)]] | alt | 4.94 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +11.1) | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0602× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 6.34 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.0811× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 8.96 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +10.4) | [[Roxadustat (drug)]] 0.05 µM 0.0928× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 9.93 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +10.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 7.88 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +12.2) | — |
| [[RKO (line)]] | wt | 15.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0540× (z -12.2) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Bendamustine (drug)]] 5 µM 0.0838× (z -9.9) |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0766× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0712× (z -9.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 3.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 5.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +10.9) | — |
| [[KATO III (line)]] | alt | 11.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0489× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 6.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 4.25 | 0 | 1 | — | [[Bendamustine (drug)]] 0.5 µM 0.0572× (z -8.5) |
| [[PANC-1 (line)]] | alt | 4.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +9.4) | — |
| [[SW48 (line)]] | wt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +9.9) | — |
| [[SW480 (line)]] | alt | 3.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +11.9) | — |
| [[A-427 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC22A1]] | +0.86 | +0.90 / +0.76 | both halves | 7e-06 |  |
| [[USP50]] | +0.85 | +0.88 / +0.72 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.84 | +0.86 / +0.70 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.83 | +0.85 / +0.74 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.83 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.82 | +0.85 / +0.69 | both halves | 7e-06 |  |
| [[NLGN3]] | +0.81 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.81 | +0.88 / +0.64 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.81 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[PILRA]] | +0.81 | +0.87 / +0.71 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.80 | +0.83 / +0.68 | both halves | 7e-06 |  |
| [[ARL9]] | +0.80 | +0.84 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PXMP4]] | B | PXMP4 activity lowers C3orf20's level | lines that do not express PXMP4 (6) vs lines expressing it (44) | 2.05× higher at baseline in the lines without PXMP4 | 0.065 | ⚠ within organs, on part of the lines; also absent: ZNF532 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.889). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.8, -13.4); signed map (18.8, 7.7). **Vector** length 98.8, 21.6% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.7 | +15.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.2 | +23.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.2 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -4.6 | -0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -5.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.6 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -5.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Bexarotene (drug)]] 5 µM |  | -2.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 194 member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:14,675,141-14,773,036 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434N1817; previously C3orf20 |
| Matched by | ensembl_id |

UniProt [Q8ND61](https://www.uniprot.org/uniprotkb/Q8ND61) carries no function annotation.

**Summary**, from NCBI Gene [84077](https://www.ncbi.nlm.nih.gov/gene/84077):

> Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25320) · Entrez [84077](https://www.ncbi.nlm.nih.gov/gene/84077) · UniProt [Q8ND61](https://www.uniprot.org/uniprotkb/Q8ND61) · Ensembl [ENSG00000131379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131379)

## Data

Gene col 5201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5201); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5201]; `tensor/DDL_lfc|DDL_z.npy` [5201]; `embed/gene_vectors.npy` [5201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5201 or target_col == 5201). Every well: [[C3orf20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C3orf20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
