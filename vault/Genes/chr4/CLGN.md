---
symbol: "CLGN"
type: "gene"
col: 7693
ensembl_id: "ENSG00000153132"
name: "calmegin"
location: "4q31.1"
module: 63
arm: "+"
pooled_cpm: 6.5
n_lines_expressing: 33
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 23
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# CLGN

*calmegin* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.01× (z +12.7, q 2e-34, up in 30 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.516× (z -5.4, q 4e-05, down in 16 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHGDH]] (+0.75, fdr 7e-06), [[GARS1]] (+0.73, fdr 7e-06), [[ULBP1]] (+0.70, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[STC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.01×** | +12.7 | 2e-34 | 30/30 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.41×** | +12.1 | 2e-31 | 15/17 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.46×** | +11.7 | 1e-29 | 9/11 (NCI-H1792, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.05×** | +9.1 | 1e-17 | 27/28 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +8.3 | 1e-14 | 12/14 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +7.7 | 2e-12 | 18/30 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.23×** | +6.5 | 5e-09 | 24/30 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.71×** | +6.2 | 4e-08 | 18/30 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +5.8 | 4e-07 | 20/30 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.94×** | +5.4 | 3e-06 | 24/30 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.3 | 7e-06 | 16/27 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.90×** | +5.2 | 8e-06 | 19/28 (NCI-H460, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +5.1 | 1e-05 | 18/30 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +4.8 | 8e-05 | 19/30 (HOP62, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.68×** | +4.1 | 0.002 | 17/28 (NCI-H460, SW480, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.002 | 14/30 (NCI-H460, H4, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.003 | 15/30 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **2.44×** | +3.8 | 0.004 | 9/23 (SW 900, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7693.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.516×** | -5.4 | 4e-05 | 16/27 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -5.0 | 2e-04 | 16/30 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.644×** | -3.6 | 0.063 | 10/30 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.659×** | -3.4 | 0.093 | 11/30 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -3.3 | 0.093 | 14/30 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -3.3 | 0.093 | 11/30 (HT-29, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.689× | -3.0 | 0.19 | 8/30 (HT-29, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.692× | -3.0 | 0.19 | 11/30 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.2 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.129× (z -11.8) |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0754× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0793× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 23.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H460 (line)]] | wt | 5.21 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.51× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -9.7) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HEC-1-A (line)]] | alt | 7.17 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.46× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.04× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 3.14 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0946× (z -9.4) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SW 900 (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -11.7) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SW480 (line)]] | alt | 2.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0641× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[A-172 (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.711 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHGDH]] | +0.75 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[GARS1]] | +0.73 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[ULBP1]] | +0.70 | +0.60 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ASNS]] | +0.68 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[CCPG1]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[SARS1]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[TCEA1]] | +0.67 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ERICH2]] | +0.67 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[IDH1]] | +0.66 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[PSAT1]] | +0.65 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[AARS1]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[DMGDH]] | +0.64 | +0.64 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STC2]] | B | CLGN activity raises STC2's level | lines that do not express CLGN (17) vs lines expressing it (33) | 2.83× lower at baseline in the lines without CLGN | 0.045 | ⚠ within organs, on part of the lines; also absent: RPS6KA6, VWDE, CLDN1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.3, 47.5); signed map (-12.5, 23.9). **Vector** length 69.6, 16.5% of its response variance represented; |z| ≥ 3 in 739 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.62 to 16); *mTORC1 signaling* (hallmark, mean cos +0.56 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.61 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +12.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +4.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.5 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | calmegin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:140,388,453-140,427,661 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Calnexin/calreticulin family |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [O14967](https://www.uniprot.org/uniprotkb/O14967) (Calmegin):

> Functions during spermatogenesis as a chaperone for a range of client proteins that are important for sperm adhesion onto the egg zona pellucida and for subsequent penetration of the zona pellucida. Required for normal sperm migration from the uterus into the oviduct. Required for normal male fertility. Binds calcium ions (By similarity).

**Summary**, from NCBI Gene [1047](https://www.ncbi.nlm.nih.gov/gene/1047):

> Calmegin is a testis-specific endoplasmic reticulum chaperone protein. CLGN may play a role in spermatogeneisis and infertility. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2060) · Entrez [1047](https://www.ncbi.nlm.nih.gov/gene/1047) · UniProt [O14967](https://www.uniprot.org/uniprotkb/O14967) · Ensembl [ENSG00000153132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153132)

## Data

Gene col 7693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7693); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7693]; `tensor/DDL_lfc|DDL_z.npy` [7693]; `embed/gene_vectors.npy` [7693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7693 or target_col == 7693). Every well: [[CLGN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLGN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
