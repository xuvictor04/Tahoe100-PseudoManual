---
symbol: "SLC15A2"
type: "gene"
col: 8686
ensembl_id: "ENSG00000163406"
name: "solute carrier family 15 member 2"
location: "3q13.33"
module: 49
arm: "+"
pooled_cpm: 9.08
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 36
n_dd_up_clean: 11
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SLC15A2

*solute carrier family 15 member 2* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +8.9, q 4e-16, up in 26 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.484× (z -7.0, q 2e-09, down in 24 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.294× (z -6.2, q 2e-07, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EAF2]] (+0.92, fdr 7e-06, ⚠ same locus), [[DNAJC25]] (+0.76, fdr 7e-06), [[SERP1]] (+0.73, fdr 7e-06), [[PGM3]] (+0.73, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +8.9 | 4e-16 | 26/38 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +7.8 | 2e-12 | 26/40 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +7.1 | 3e-10 | 28/45 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +6.4 | 2e-08 | 23/39 (Panc 03.27, SW1417, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +5.6 | 2e-06 | 23/44 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +5.3 | 1e-05 | 18/42 (LOX-IMVI, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +4.4 | 7e-04 | 19/44 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.3 | 0.001 | 19/46 (SW1417, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.009 | 12/46 (SW1417, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.048 | 12/43 (SW1417, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.067 | 12/44 (A-172, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8686.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.484×** | -7.0 | 2e-09 | 24/31 (SW 900, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.294×** | -6.2 | 2e-07 | 29/43 (HCT15, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.547×** | -5.8 | 1e-06 | 25/46 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.554×** | -5.7 | 2e-06 | 26/44 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.572×** | -5.4 | 9e-06 | 24/44 (A498, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.574×** | -5.3 | 9e-06 | 24/44 (LS 180, RPMI-7951, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.586×** | -5.1 | 2e-05 | 21/46 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.607×** | -4.8 | 1e-04 | 20/41 (SW 900, KATO III, …) | all doses, stronger at high dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.616×** | -4.7 | 2e-04 | 21/43 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.620×** | -4.6 | 2e-04 | 18/44 (HT-29, J82, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.622×** | -4.6 | 3e-04 | 20/43 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.623×** | -4.5 | 3e-04 | 22/46 (LoVo, H4, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.628×** | -4.5 | 3e-04 | 17/46 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.416×** | -4.4 | 4e-04 | 19/40 (SW 900, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.644×** | -4.2 | 9e-04 | 21/46 (LS 180, HCT15, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -3.9 | 0.003 | 16/46 (HS-578T, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -3.8 | 0.005 | 16/43 (CFPAC-1, HS-578T, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.52 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.105× (z -11.8) |
| [[J82 (line)]] | alt | 5.04 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +8.6) | [[Belumosudil (drug)]] 5 µM 0.0630× (z -9.4) |
| [[KATO III (line)]] | alt | 28.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0628× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[AsPC-1 (line)]] | alt | 5.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.158× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0490× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[H4 (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0428× (z -11.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0402× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -10.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 4.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.127× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EAF2]] | +0.92 | +0.93 / +0.92 | both halves | 7e-06 | ⚠ same locus (7.9 kb, same strand: neighbours can correlate without regulation) |
| [[DNAJC25]] | +0.76 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[SERP1]] | +0.73 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[PGM3]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[SRP54]] | +0.72 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.71 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[MCEE]] | +0.71 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[COG6]] | +0.69 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[GMPPA]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[TBC1D8B]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[OSTC]] | +0.67 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[DNAJB9]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[UFM1]] | +0.65 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC15A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MCTP2]] | B | MCTP2 activity raises SLC15A2's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.73× lower at baseline in the lines without MCTP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[GALNT3]] | B | GALNT3 activity raises SLC15A2's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without GALNT3 | 0.050 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[AGR2]] | B | AGR2 activity raises SLC15A2's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.77× lower at baseline in the lines without AGR2 | 0.076 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[ESRP1]] | B | ESRP1 activity raises SLC15A2's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 1.84× lower at baseline in the lines without ESRP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, -35.7); signed map (-51.1, 12.7). **Vector** length 103, 24.7% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.51 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.51 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +8.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +7.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.7 | +1.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -3.8 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -4.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -6.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.3 | -5.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.2 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 15 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:121,894,401-121,944,188 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEPT2 |
| Gene groups (HGNC) | Solute carrier family 15 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16348](https://www.uniprot.org/uniprotkb/Q16348) (Solute carrier family 15 member 2):

> Proton-coupled amino-acid transporter that transports oligopeptides of 2 to 4 amino acids with a preference for dipeptides. Transports neutral and anionic dipeptides with a proton to peptide stoichiometry of 2:1 or 3:1 (By similarity). In kidney, involved in the absorption of circulating di- and tripeptides from the glomerular filtrate. Can also transport beta-lactam antibiotics, such as the aminocephalosporin cefadroxil, and other antiviral and anticancer drugs. Transports the dipeptide-like …

**Summary**, from NCBI Gene [6565](https://www.ncbi.nlm.nih.gov/gene/6565):

> The mammalian kidney expresses a proton-coupled peptide transporter that is responsible for the absorption of small peptides, as well as beta-lactam antibiotics and other peptide-like drugs, from the tubular filtrate. This transporter, SLC15A2, belongs to the same gene family as SLC15A1 (MIM 600544), the proton-coupled peptide transporter found in the small intestine (Liu et al, 1995 [PubMed 7756356]).[supplied by OMIM, Feb 2011]

**Accessions** — [HGNC:10921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10921) · Entrez [6565](https://www.ncbi.nlm.nih.gov/gene/6565) · UniProt [Q16348](https://www.uniprot.org/uniprotkb/Q16348) · Ensembl [ENSG00000163406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163406)

## Data

Gene col 8686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8686); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8686]; `tensor/DDL_lfc|DDL_z.npy` [8686]; `embed/gene_vectors.npy` [8686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8686 or target_col == 8686). Every well: [[SLC15A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC15A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
