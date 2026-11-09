---
symbol: "POLR1G"
type: "gene"
col: 3954
ensembl_id: "ENSG00000117877"
name: "RNA polymerase I subunit G"
location: "19q13.32"
module: 5
arm: "+"
pooled_cpm: 12.37
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# POLR1G

*RNA polymerase I subunit G* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.11× (z +11.3, q 7e-27, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +7.9, q 4e-13, up in 30 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.651× (z -4.9, q 7e-04, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYAR]] (+0.77, fdr 7e-06), [[NOP16]] (+0.74, fdr 7e-06), [[PDCD11]] (+0.74, fdr 7e-06); moves opposite to [[RNF11]] (-0.58, fdr 1e-05), [[RNF10]] (-0.56, fdr 1e-05), [[ABHD4]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3954.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **4.11×** | +11.3 | 7e-27 | 43/47 (HOP62, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **3.68×** | +10.4 | 5e-23 | 43/47 (HOP62, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **3.47×** | +10.0 | 4e-21 | 46/47 (HOP62, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +7.9 | 4e-13 | 30/43 (A549, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.69×** | +7.6 | 3e-12 | 33/39 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **2.34×** | +6.8 | 1e-09 | 23/36 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **2.15×** | +5.9 | 3e-07 | 12/17 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.08×** | +5.9 | 3e-07 | 30/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +5.1 | 3e-05 | 27/46 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.9 | 4e-05 | 26/48 (J82, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +4.4 | 6e-04 | 26/42 (CFPAC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.75×** | +4.3 | 8e-04 | 22/45 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.66×** | +4.1 | 0.002 | 21/46 (Panc 03.27, J82, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.62×** | +3.9 | 0.004 | 18/44 (J82, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.60×** | +3.8 | 0.006 | 16/41 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.37×** | +3.6 | 0.011 | 20/43 (MIA PaCa-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.14×** | +3.2 | 0.040 | 15/44 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.99×** | +2.9 | 0.092 | 9/37 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3954.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM |  | **0.651×** | -4.9 | 7e-04 | 27/48 (AN3 CA, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.601×** | -4.0 | 0.017 | 23/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.616×** | -3.6 | 0.064 | 21/47 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.650×** | -3.4 | 0.081 | 19/48 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | 0.464× | -3.2 | 0.15 | 9/47 (AsPC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.673× | -3.0 | 0.22 | 18/44 (HepG2/C3A, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.75 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 17.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.90× (z +9.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 7.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.510× (z -10.8) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 4.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.08× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0502× (z -11.6) |
| [[SNU-423 (line)]] | alt | 6.56 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.0682× (z -9.3) |
| [[A-172 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYAR]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | STRING 634 |
| [[NOP16]] | +0.74 | +0.68 / +0.81 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.74 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.69 | +0.65 / +0.80 | both halves | 7e-06 | STRING 700 |
| [[POLR1E]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 | same gene group; pathway: B-WICH complex positively regulates rRNA expression; STRING 999 |
| [[RRP1]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 | STRING 791 |
| [[TWNK]] | +0.68 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[NOP2]] | +0.67 | +0.59 / +0.72 | both halves | 7e-06 | STRING 461 |
| [[UTP14A]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 | STRING 573 |
| [[PWP2]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 | STRING 400 |
| [[NIFK]] | +0.66 | +0.60 / +0.73 | both halves | 7e-06 | STRING 799 |
| [[RRS1]] | +0.65 | +0.66 / +0.67 | both halves | 7e-06 | STRING 765 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF11]] | -0.58 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[RNF10]] | -0.56 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[ABHD4]] | -0.55 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[RAB21]] | -0.53 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[BPNT1]] | -0.52 | -0.39 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.5, -38.4); signed map (-2.4, -47.8). **Vector** length 86.0, 21.7% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.58 to 13); *rRNA processing* (reactome, mean cos +0.51 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.1 | +10.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.0 | +11.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +2.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.4 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | -3.2 | +5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase I subunit G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,406,644-45,410,737 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASE-1, CAST, PAF49, RPA34, A34.5; previously CD3EAP |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 9 pathways, smallest: RNA Polymerase I Transcription Termination; B-WICH complex positively regulates rRNA expression; RNA Polymerase I Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [O15446](https://www.uniprot.org/uniprotkb/O15446) (DNA-directed RNA polymerase I subunit RPA34):

> Component of RNA polymerase I (Pol I), a DNA-dependent RNA polymerase which synthesizes ribosomal RNA precursors using the four ribonucleoside triphosphates as substrates. Involved in UBTF-activated transcription, presumably at a step following PIC formation.; [Isoform 2]: Has been described as a component of preformed T-cell receptor (TCR) complex.

**Summary**, from NCBI Gene [10849](https://www.ncbi.nlm.nih.gov/gene/10849):

> Enables RNA binding activity. Involved in transcription elongation by RNA polymerase I and transcription initiation at RNA polymerase I promoter. Located in fibrillar center and nucleoplasm. Part of RNA polymerase I complex. Implicated in multiple myeloma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24219) · Entrez [10849](https://www.ncbi.nlm.nih.gov/gene/10849) · UniProt [O15446](https://www.uniprot.org/uniprotkb/O15446) · Ensembl [ENSG00000117877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117877)

## Data

Gene col 3954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3954); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3954]; `tensor/DDL_lfc|DDL_z.npy` [3954]; `embed/gene_vectors.npy` [3954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3954 or target_col == 3954). Every well: [[POLR1G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR1G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
