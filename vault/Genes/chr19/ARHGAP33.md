---
symbol: "ARHGAP33"
type: "gene"
col: 52
ensembl_id: "ENSG00000004777"
name: "Rho GTPase activating protein 33"
location: "19q13.12"
module: 67
arm: "+"
pooled_cpm: 5.95
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# ARHGAP33

*Rho GTPase activating protein 33* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.73× (z +5.4, q 4e-05, up in 5 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.41× (z +3.8, q 0.017, up in 13 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.505× (z -7.5, q 4e-11, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQGAP3]] (+0.69, fdr 7e-06), [[CNTROB]] (+0.69, fdr 7e-06), [[KIFC1]] (+0.68, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 52.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.4 | 4e-05 | 5/13 (HT-29, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +5.0 | 1e-04 | 8/30 (NCI-H23, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +3.9 | 0.017 | 13/39 (LoVo, NCI-H2030, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.017 | 13/45 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.070 | 9/43 (HEC-1-A, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.074 | 10/46 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.33× | +3.2 | 0.11 | 12/46 (KATO III, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.32× | +3.1 | 0.14 | 3/46 (HS-578T, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 52.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.505×** | -7.5 | 4e-11 | 25/45 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -5.1 | 8e-05 | 19/36 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.631×** | -5.0 | 8e-05 | 18/46 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.638×** | -4.9 | 1e-04 | 21/45 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -4.6 | 4e-04 | 20/45 (COLO 205, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -4.5 | 8e-04 | 18/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -3.9 | 0.007 | 17/38 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.703×** | -3.9 | 0.007 | 17/37 (HT-29, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.703×** | -3.9 | 0.007 | 9/45 (HEC-1-A, NCI-H661, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.781×** | -3.8 | 0.008 | 15/46 (A549, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.715×** | -3.7 | 0.012 | 17/44 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.718×** | -3.6 | 0.014 | 16/43 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.724×** | -3.5 | 0.018 | 14/44 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.701×** | -3.5 | 0.023 | 12/44 (COLO 205, NCI-H2347, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.723×** | -3.4 | 0.030 | 16/43 (A-427, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.743×** | -3.3 | 0.040 | 10/41 (NCI-H460, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 52. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Busulfan (drug)]] 0.05 µM 0.0665× (z -10.8) |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0765× (z -9.2) ⚠ toxic; unreliable plate only |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.198× (z -8.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 5.59 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0765× (z -10.0) |
| [[SW480 (line)]] | alt | 7.14 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0961× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 52), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQGAP3]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | pathway: CDC42 GTPase cycle; STRING 429 |
| [[CNTROB]] | +0.69 | +0.72 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[KIFC1]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[RACGAP1]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 | pathway: CDC42 GTPase cycle |
| [[KIF22]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SPAG5]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[AURKB]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ARHGAP11B]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 | same gene group; pathway: CDC42 GTPase cycle |
| [[CIT]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 | pathway: RAC1 GTPase cycle |
| [[CDCA3]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[NCAPH2]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CHTF18]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises ARHGAP33's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without PIMREG | 0.057 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers ARHGAP33's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[AURKB]] | C | AURKB activity raises ARHGAP33's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without AURKB | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises ARHGAP33's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without PBK | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.4, -54.5); signed map (-47.7, -41.5). **Vector** length 74.2, 12.6% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.55 to 12); *G2/M checkpoint* (hallmark, mean cos +0.53 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.6 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Saquinavir (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.5 | +1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,774,532-35,788,822 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39019, TCGAP; previously SNX26 |
| Gene groups (HGNC) | Rho GTPase activating proteins; SH3 domain containing |
| Reactome | 6 pathways, smallest: RHOQ GTPase cycle; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O14559](https://www.uniprot.org/uniprotkb/O14559) (Rho GTPase-activating protein 33):

> May be involved in several stages of intracellular trafficking. Could play an important role in the regulation of glucose transport by insulin. May act as a downstream effector of RHOQ/TC10 in the regulation of insulin-stimulated glucose transport (By similarity).

**Summary**, from NCBI Gene [115703](https://www.ncbi.nlm.nih.gov/gene/115703):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. Alternative splice variants encoding different isoforms have been identified in this gene. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:23085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23085) · Entrez [115703](https://www.ncbi.nlm.nih.gov/gene/115703) · UniProt [O14559](https://www.uniprot.org/uniprotkb/O14559) · Ensembl [ENSG00000004777](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004777)

## Data

Gene col 52: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 52); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 52, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 52]; `tensor/DDL_lfc|DDL_z.npy` [52]; `embed/gene_vectors.npy` [52]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 52 or target_col == 52). Every well: [[ARHGAP33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
