---
symbol: "CCDC86"
type: "gene"
col: 3116
ensembl_id: "ENSG00000110104"
name: "coiled-coil domain containing 86"
location: "11q12.2"
module: 1
arm: "+"
pooled_cpm: 10.42
n_lines_expressing: 50
n_dd_up: 44
n_dd_down: 4
n_dd_up_clean: 28
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CCDC86

*coiled-coil domain containing 86* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.00× (z +12.3, q 6e-32, up in 18 of 20 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.46× (z +10.5, q 4e-23, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.630× (z -7.7, q 7e-12, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIP7]] (+0.76, fdr 7e-06), [[BYSL]] (+0.76, fdr 7e-06), [[ABCF2]] (+0.75, fdr 7e-06); moves opposite to [[HDAC5]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MEX3A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.00×** | +12.3 | 6e-32 | 18/20 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.46×** | +10.5 | 4e-23 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.33×** | +9.8 | 2e-20 | 28/37 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +9.5 | 3e-19 | 31/46 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.17×** | +9.0 | 2e-17 | 44/47 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.08×** | +8.5 | 2e-15 | 34/47 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.33×** | +8.5 | 2e-15 | 22/28 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +8.3 | 5e-15 | 31/40 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +7.8 | 4e-13 | 28/46 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +7.6 | 2e-12 | 25/45 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.94×** | +7.4 | 9e-12 | 29/40 (SW480, Hs 766T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +7.2 | 4e-11 | 31/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.85×** | +6.9 | 3e-10 | 31/46 (NCI-H1792, H4, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +6.3 | 1e-08 | 31/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.72×** | +6.1 | 5e-08 | 28/45 (SW1417, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.63×** | +5.4 | 2e-06 | 22/45 (NCI-H1573, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +5.3 | 2e-06 | 21/47 (A549, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **2.40×** | +5.3 | 3e-06 | 24/44 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.8 | 3e-05 | 16/48 (CFPAC-1, J82, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.52×** | +4.8 | 3e-05 | 25/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.16×** | +4.7 | 6e-05 | 22/44 (PANC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.09×** | +4.5 | 2e-04 | 17/44 (SW1417, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.630×** | -7.7 | 7e-12 | 35/48 (SW1417, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.594×** | -6.2 | 2e-07 | 29/46 (SHP-77, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.530×** | -3.9 | 0.017 | 16/46 (NCI-H2030, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 5 µM |  | **0.816×** | -3.4 | 0.081 | 12/47 (RPMI-7951, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.57× (z +8.6) | — |
| [[J82 (line)]] | alt | 16.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 20.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 4.92 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.0675× (z -8.7) |
| [[C32 (line)]] | wt | 8.06 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0834× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.05× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[PANC-1 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SHP-77 (line)]] | alt | 6.87 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0850× (z -9.1) |
| [[A-172 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIP7]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 | STRING 655 |
| [[BYSL]] | +0.76 | +0.79 / +0.73 | both halves | 7e-06 | STRING 564 |
| [[ABCF2]] | +0.75 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[RRS1]] | +0.75 | +0.80 / +0.70 | both halves | 7e-06 | STRING 490 |
| [[DHX37]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[UTP15]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 | STRING 514 |
| [[WDR77]] | +0.72 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[DHX33]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[C1orf109]] | +0.71 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[PNO1]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[MRM1]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC5]] | -0.58 | -0.57 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEX3A]] | B | MEX3A activity raises CCDC86's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without MEX3A | 0.092 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.2, -36.3); signed map (-0.9, -45.3). **Vector** length 79.5, 16.5% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.52 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.53 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +5.0 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.9 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +7.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +5.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -6.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 86 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:60,842,113-60,851,081 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2574, cyclon, Cgr1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6F5](https://www.uniprot.org/uniprotkb/Q9H6F5) (Coiled-coil domain-containing protein 86):

> Required for proper chromosome segregation during mitosis and error-free mitotic progression.

**Summary**, from NCBI Gene [79080](https://www.ncbi.nlm.nih.gov/gene/79080):

> Enables RNA binding activity. Involved in chromosome segregation and mitotic nuclear division. Located in chromosome; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28359) · Entrez [79080](https://www.ncbi.nlm.nih.gov/gene/79080) · UniProt [Q9H6F5](https://www.uniprot.org/uniprotkb/Q9H6F5) · Ensembl [ENSG00000110104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110104)

## Data

Gene col 3116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3116); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3116]; `tensor/DDL_lfc|DDL_z.npy` [3116]; `embed/gene_vectors.npy` [3116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3116 or target_col == 3116). Every well: [[CCDC86 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC86.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
