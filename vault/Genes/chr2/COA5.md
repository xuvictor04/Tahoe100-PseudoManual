---
symbol: "COA5"
type: "gene"
col: 11413
ensembl_id: "ENSG00000183513"
name: "cytochrome c oxidase assembly factor 5"
location: "2q11.2"
module: 220
arm: "+"
pooled_cpm: 11.85
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# COA5

*cytochrome c oxidase assembly factor 5* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.55× (z +5.9, q 3e-06, up in 26 of 42 measured lines) ⚠ transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.33× (z +5.3, q 3e-05, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.655× (z -8.0, q 5e-13, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX2]] (+0.63, fdr 2e-05), [[SNRNP35]] (+0.61, fdr 1e-05), [[MRPS14]] (+0.60, fdr 1e-05); moves opposite to [[TLN1]] (-0.45, fdr 3e-05), [[IQGAP1]] (-0.45, fdr 3e-05), [[CSPG5]] (-0.44, fdr 8e-05).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF594-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +5.9 | 3e-06 | 26/42 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +5.3 | 3e-05 | 25/48 (HS-578T, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.2 | 4e-05 | 22/40 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.6 | 4e-04 | 10/22 (NCI-H460, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.6 | 4e-04 | 19/35 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.9 | 0.009 | 8/42 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +3.7 | 0.016 | 16/29 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.019 | 15/47 (A-427, NCI-H23, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.037 | 9/43 (COLO 205, LoVo, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.655×** | -8.0 | 5e-13 | 33/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -7.2 | 2e-10 | 29/44 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.413×** | -5.7 | 2e-06 | 23/43 (COLO 205, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.690×** | -5.0 | 8e-05 | 21/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.467×** | -5.0 | 8e-05 | 23/48 (NCI-H23, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.721×** | -4.1 | 0.003 | 21/47 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.742×** | -4.0 | 0.005 | 15/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.748×** | -3.9 | 0.007 | 16/47 (HT-29, H4, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.768×** | -3.6 | 0.024 | 8/47 (Hs 766T, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.790×** | -3.2 | 0.086 | 11/47 (HT-29, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.100× (z -11.0) ⚠ transcription drop |
| [[H4 (line)]] | wt | 11.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0873× (z -8.7) |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.143× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 8.56 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0824× (z -9.2) |
| [[J82 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0828× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[LS 180 (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0800× (z -9.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0747× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.2) |
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -8.9) |
| [[A-172 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX2]] | +0.63 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SNRNP35]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[MRPS14]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ZNF493]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SPIN2B]] | +0.56 | +0.35 / +0.68 | both halves | 1e-04 |  |
| [[DTWD1]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ZNF12]] | +0.53 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[VAMP2]] | +0.53 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[ABHD13]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[C6orf89]] | +0.51 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[TAF8]] | +0.51 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[NISCH]] | +0.51 | +0.27 / +0.63 | both halves | 3e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLN1]] | -0.45 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[IQGAP1]] | -0.45 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CSPG5]] | -0.44 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[HCN2]] | -0.44 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[TPM3]] | -0.43 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[KIF1B]] | -0.43 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[CYFIP1]] | -0.43 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TTC36]] | -0.43 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[MAP4]] | -0.42 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[PRPSAP1]] | -0.41 | -0.33 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594-DT]] | B | ZNF594-DT activity raises COA5's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.30× lower at baseline in the lines without ZNF594-DT | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-41.8, 16.3); signed map (-11.5, -16.0). **Vector** length 53.2, 7.67% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.2 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +5.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.3 | +5.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.0 | -8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.7 | -5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -5.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:98,599,314-98,608,515 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC52110, FLJ27524, Pet191; previously C2orf64 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WW8](https://www.uniprot.org/uniprotkb/Q86WW8) (Cytochrome c oxidase assembly factor 5):

> Assembly factor for cytochrome c oxidase (respiratory chain complex IV). Stabilizes an early formation of cytochrome c oxidase assembly factors, until it is displaced by the metallochaperone copper-delivery protein COX17.

**Summary**, from NCBI Gene [493753](https://www.ncbi.nlm.nih.gov/gene/493753):

> This gene encodes an ortholog of yeast Pet191, which in yeast is a subunit of a large oligomeric complex associated with the mitochondrial inner membrane, and required for the assembly of the cytochrome c oxidase complex. Mutations in this gene are associated with mitochondrial complex IV deficiency, a disorder of the mitochondrial respiratory chain with heterogeneous clinical manifestations, ranging from isolated myopathy to a severe disease affecting several tissues and organs. [provided by …

**Accessions** — [HGNC:33848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33848) · Entrez [493753](https://www.ncbi.nlm.nih.gov/gene/493753) · UniProt [Q86WW8](https://www.uniprot.org/uniprotkb/Q86WW8) · Ensembl [ENSG00000183513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183513)

## Data

Gene col 11413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11413); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11413]; `tensor/DDL_lfc|DDL_z.npy` [11413]; `embed/gene_vectors.npy` [11413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11413 or target_col == 11413). Every well: [[COA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
