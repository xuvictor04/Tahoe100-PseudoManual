---
symbol: "MRPS15"
type: "gene"
col: 3853
ensembl_id: "ENSG00000116898"
name: "mitochondrial ribosomal protein S15"
location: "1p34.3"
module: 72
arm: "+"
pooled_cpm: 20.09
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# MRPS15

*mitochondrial ribosomal protein S15* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.43× (z +13.9, q 7e-41, up in 39 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +7.9, q 3e-13, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.752× (z -4.5, q 0.004, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BABAM1]] (+0.71, fdr 7e-06), [[PSMB5]] (+0.69, fdr 7e-06), [[PSMB2]] (+0.66, fdr 7e-06); moves opposite to [[PIM3]] (-0.62, fdr 2e-05), [[IER2]] (-0.61, fdr 1e-05), [[N4BP3]] (-0.56, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 16 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.43×** | +13.9 | 7e-41 | 39/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.94×** | +11.7 | 6e-29 | 30/32 (Hs 766T, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.27×** | +8.1 | 1e-13 | 29/36 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.9 | 3e-13 | 32/47 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.86×** | +7.0 | 4e-10 | 42/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.78×** | +6.5 | 8e-09 | 36/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +6.4 | 2e-08 | 39/46 (HOP62, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +6.2 | 3e-08 | 30/43 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.57×** | +5.1 | 3e-05 | 26/46 (SW1417, AsPC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.24×** | +4.7 | 1e-04 | 27/39 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.50×** | +4.6 | 2e-04 | 25/44 (SW1417, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.52×** | +4.5 | 3e-04 | 28/47 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.4 | 4e-04 | 24/47 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.88×** | +3.7 | 0.009 | 20/46 (SW1417, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.40×** | +3.7 | 0.009 | 20/45 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.010 | 19/48 (A-427, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3853.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.752×** | -4.5 | 0.004 | 26/47 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.781×** | -3.9 | 0.027 | 25/48 (SW 1088, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 16.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 23.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 27.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 21.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.27× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BABAM1]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[PSMB5]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PSMB2]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[MRPL18]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 888 |
| [[QRSL1]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[UBE2L3]] | +0.64 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[RCC1L]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[KMT2D]] | +0.62 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[TOR1A]] | +0.62 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[GLB1]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[TOR3A]] | +0.61 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[COA6]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIM3]] | -0.62 | -0.71 / -0.48 | both halves | 2e-05 |  |
| [[IER2]] | -0.61 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[N4BP3]] | -0.56 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[LMNA]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[UGCG]] | -0.55 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[KLF2]] | -0.54 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[DHRS2]] | -0.54 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[CDKN2D]] | -0.52 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[JUND]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[LIMA1]] | -0.51 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[NR4A1]] | -0.51 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[SPAG9]] | -0.51 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MRPS15's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.1, -10.5); signed map (-25.3, -25.0). **Vector** length 59.1, 11.5% of its response variance represented; |z| ≥ 3 in 759 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *proteasome* (control, mean cos +0.51 to 11); *Regulation of activated PAK-2p34 by proteasome mediated degradation* (reactome, mean cos +0.51 to 11); *Regulation of ornithine decarboxylase (ODC)* (reactome, mean cos +0.51 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.1 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.1 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:36,455,718-36,464,384 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11564, uS15m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [P82914](https://www.uniprot.org/uniprotkb/P82914) carries no function annotation.

**Summary**, from NCBI Gene [64960](https://www.ncbi.nlm.nih.gov/gene/64960):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14504) · Entrez [64960](https://www.ncbi.nlm.nih.gov/gene/64960) · UniProt [P82914](https://www.uniprot.org/uniprotkb/P82914) · Ensembl [ENSG00000116898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116898)

## Data

Gene col 3853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3853); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3853]; `tensor/DDL_lfc|DDL_z.npy` [3853]; `embed/gene_vectors.npy` [3853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3853 or target_col == 3853). Every well: [[MRPS15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
