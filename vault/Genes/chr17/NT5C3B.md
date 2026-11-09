---
symbol: "NT5C3B"
type: "gene"
col: 6567
ensembl_id: "ENSG00000141698"
name: "5'-nucleotidase, cytosolic IIIB"
location: "17q21.2"
module: 221
arm: "+"
pooled_cpm: 13.1
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/221"]
generated_by: "tahoemap"
---

# NT5C3B

*5'-nucleotidase, cytosolic IIIB* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.14× (z +10.1, q 3e-21, up in 29 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.39× (z +6.2, q 1e-07, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.644× (z -8.3, q 6e-14, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRHPR]] (+0.63, fdr 1e-05), [[HMGN4]] (+0.59, fdr 1e-05), [[LZTR1]] (+0.56, fdr 1e-05); moves opposite to [[PRKCA]] (-0.50, fdr 4e-05), [[HMGB1]] (-0.47, fdr 2e-04), [[ENSA]] (-0.45, fdr 1e-04).
> It is in [[Module 221]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRP3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[UBE2Q2P1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +10.1 | 3e-21 | 29/35 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +8.2 | 5e-14 | 12/19 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +6.2 | 1e-07 | 24/47 (CFPAC-1, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +4.9 | 1e-04 | 10/26 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +4.6 | 5e-04 | 18/40 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.006 | 19/46 (H4, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.008 | 10/44 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.020 | 11/44 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.5 | 0.027 | 11/40 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.064 | 10/46 (NCI-H2030, HOP62, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.074 | 9/45 (C32, HOP62, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.42× | +3.0 | 0.12 | 6/36 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6567.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.644×** | -8.3 | 6e-14 | 29/46 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.683×** | -5.1 | 1e-04 | 26/46 (A498, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.728×** | -4.2 | 0.005 | 20/46 (A-427, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.537×** | -3.7 | 0.026 | 13/47 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.581× | -3.3 | 0.12 | 12/42 (NCI-H2030, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -9.2) |
| [[J82 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -12.6) |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~3% of this change |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRHPR]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[HMGN4]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[LZTR1]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[RTCA]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[FBXO44]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC24]] | +0.54 | +0.34 / +0.67 | both halves | 1e-04 |  |
| [[ENTREP3]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PLD2]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[MKRN2]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[JOSD2]] | +0.53 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[DNAJC19]] | +0.52 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[FAHD2B]] | +0.52 | +0.34 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKCA]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[HMGB1]] | -0.47 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[ENSA]] | -0.45 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[CFL1]] | -0.45 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[OPA3]] | -0.44 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[PFN1]] | -0.44 | -0.38 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP3]] | B | LRP3 activity raises NT5C3B's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without LRP3 | 0.045 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2Q2P1]] | C | NT5C3B's natural level strengthens UBE2Q2P1's drug response | NT5C3B's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.11; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 221]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.2, -10.6); signed map (-34.0, -20.7). **Vector** length 52.0, 7.70% of its response variance represented; |z| ≥ 3 in 610 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.6 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.2 | +4.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -5.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.9 | -2.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -0.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | 5'-nucleotidase, cytosolic IIIB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,825,057-41,836,260 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20781, cN-IIIB; previously NT5C3L |
| Reactome | 3 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969T7](https://www.uniprot.org/uniprotkb/Q969T7) (7-methylguanosine phosphate-specific 5'-nucleotidase):

> Specifically hydrolyzes 7-methylguanosine monophosphate (m(7)GMP) to 7-methylguanosine and inorganic phosphate. The specific activity for m(7)GMP may protect cells against undesired salvage of m(7)GMP and its incorporation into nucleic acids. Also has weak activity for CMP. UMP and purine nucleotides are poor substrates.

**Summary**, from NCBI Gene [115024](https://www.ncbi.nlm.nih.gov/gene/115024):

> Predicted to enable 5'-nucleotidase activity. Predicted to be involved in nuclear-transcribed mRNA catabolic process, deadenylation-dependent decay. Predicted to be located in cytosol. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28300) · Entrez [115024](https://www.ncbi.nlm.nih.gov/gene/115024) · UniProt [Q969T7](https://www.uniprot.org/uniprotkb/Q969T7) · Ensembl [ENSG00000141698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141698)

## Data

Gene col 6567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6567); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6567]; `tensor/DDL_lfc|DDL_z.npy` [6567]; `embed/gene_vectors.npy` [6567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6567 or target_col == 6567). Every well: [[NT5C3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NT5C3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
