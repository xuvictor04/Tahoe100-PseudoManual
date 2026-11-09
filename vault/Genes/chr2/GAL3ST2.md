---
symbol: "GAL3ST2"
type: "gene"
col: 7789
ensembl_id: "ENSG00000154252"
name: "galactose-3-O-sulfotransferase 2"
location: "2q37.3"
module: 47
arm: "+"
pooled_cpm: 2.24
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# GAL3ST2

*galactose-3-O-sulfotransferase 2* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.44× (z +8.5, q 1e-14, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +7.4, q 5e-11, up in 18 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.221× (z -10.8, q 3e-24, down in 33 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO15A]] (+0.67, fdr 7e-06), [[AZU1]] (+0.66, fdr 8e-06), [[C19orf38]] (+0.66, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SSPOP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +8.5 | 1e-14 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +7.4 | 5e-11 | 18/27 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.46×** | +6.4 | 2e-08 | 21/42 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +5.7 | 1e-06 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +4.6 | 4e-04 | 2/8 (HEC-1-A, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +3.5 | 0.041 | 4/22 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.2 | 0.097 | 2/17 (HOP62, A-172) | rises with dose |  |
| [[Ritonavir (drug)]] 5 µM |  | 1.37× | +3.2 | 0.11 | 3/36 (SW480, SW1417, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.55× | +3.1 | 0.11 | 4/45 (PANC-1, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7789.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.221×** | -10.8 | 3e-24 | 33/44 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.335×** | -7.8 | 2e-12 | 25/37 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -5.3 | 2e-05 | 18/32 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.570×** | -4.0 | 0.009 | 21/41 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.569×** | -3.9 | 0.013 | 12/40 (LoVo, COLO 205, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -3.8 | 0.013 | 15/17 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.593×** | -3.7 | 0.016 | 13/37 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM |  | **0.550×** | -3.3 | 0.069 | 7/38 (SW1417, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -3.2 | 0.082 | 9/30 (HOP62, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.729×** | -3.2 | 0.082 | 14/37 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.631× | -3.1 | 0.10 | 11/31 (A498, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.77 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0837× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0849× (z -9.2) |
| [[PANC-1 (line)]] | alt | 2.63 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0825× (z -8.6) |
| [[A498 (line)]] | wt | 4.95 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 3.06 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0689× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 5.36 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0850× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.620 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.864 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.581 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.999 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.755 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.662 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.648 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO15A]] | +0.67 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[AZU1]] | +0.66 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[C19orf38]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[FSCN2]] | +0.66 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[STAC3]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[HPN]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ASIC4]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[CHADL]] | +0.65 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[SLC7A9]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[COL20A1]] | +0.64 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[ZDHHC11]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[C16orf95]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSPOP]] | B | SSPOP activity raises GAL3ST2's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.43× lower at baseline in the lines without SSPOP | 0.064 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[STK31]] | B | STK31 activity lowers GAL3ST2's level | lines that do not express STK31 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without STK31 | 0.073 | ⚠ within organs, on part of the lines; also absent: HPSE, LTBP4, STRIP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.4, -13.1); signed map (19.1, 14.3). **Vector** length 43.1, 5.34% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +4.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -10.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.2 | -0.7 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | galactose-3-O-sulfotransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,776,822-241,804,287 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GP3ST |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3Q3](https://www.uniprot.org/uniprotkb/Q9H3Q3) (Galactose-3-O-sulfotransferase 2):

> Catalyzes the transfer of a sulfate group from 3'-phosphoadenylyl sulfate (PAPS) to the C-3 hydroxyl group of terminal non-reducing beta-galactosyl residues. Acts both on type 1 (Gal-beta-1,3-GlcNAc-R) and type 2 (Gal-beta-1,4-GlcNAc-R) chains with similar efficiency. Displays species-dependent substrate specificity. Participates in galactose sulfation and shows substrate preference for structures such as lactose, lacto-N-tetraose (Lc4), lacto-N-neotetraose (nLc4), the Gal-beta-1,4-GlcNAc-beta …

**Summary**, from NCBI Gene [64090](https://www.ncbi.nlm.nih.gov/gene/64090):

> This gene encodes a member of the galactose-3-O-sulfotransferase protein family. The product of this gene catalyzes sulfonation by transferring a sulfate group to the hydroxyl at C-3 of nonreducing beta-galactosyl residues, and it can act on both type 1 and type 2 (Galbeta 1-3/1-4GlcNAc-R) oligosaccharides with similar efficiencies, and on core 1 glycans. This enzyme has been implicated in tumor metastasis processes. This gene is different from the GAL3ST3 gene located on chromosome 11, which …

**Accessions** — [HGNC:24869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24869) · Entrez [64090](https://www.ncbi.nlm.nih.gov/gene/64090) · UniProt [Q9H3Q3](https://www.uniprot.org/uniprotkb/Q9H3Q3) · Ensembl [ENSG00000154252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154252)

## Data

Gene col 7789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7789); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7789]; `tensor/DDL_lfc|DDL_z.npy` [7789]; `embed/gene_vectors.npy` [7789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7789 or target_col == 7789). Every well: [[GAL3ST2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAL3ST2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
