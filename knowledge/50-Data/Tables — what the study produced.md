---
type: index
tags: [index, data]
generated_by: knowledge/_build/build_vault.py
---

# Tables — what the study actually produced

Paths are relative to the repository root. The vault links to these rather than copying them, so there is one copy of every number.

## The three headline correlation tables

| Table | What it holds |
|---|---|
| `mg53_p53/findings/tables/tableA_wt_p53_targets.csv` | MG53 against p53 targets in TP53-wild-type lines |
| `mg53_p53/findings/tables/tableB_upstream_mg53.csv` | what raises and lowers MG53 |
| `mg53_p53/findings/tables/tableC_mutants_by_activity.csv` | MG53 against p53 output, split by how much p53 activity each mutant retains |

## Per gene

| Table | What it holds |
|---|---|
| `mg53_p53/findings/tables/p53_effectors_per_gene.csv` | the 29 canonical p53 effectors, with direction and signed MG53 effect |
| `mg53_p53/findings/tables/tableD_p53_target_genes.csv` | all 195 program genes, 70+ columns |
| `mg53_p53/findings/tables/tableD_signed_tally.csv` | the signed split: 35 toward more p53 output, 32 toward less |
| `mg53_p53/findings/tables/tableD_top_mg53_partners.csv` | the 100 genes MG53 tracks most strongly genome-wide |

## Per cell line

| Table | What it holds |
|---|---|
| `mg53_p53/findings/tables/per_line_p53_state.csv` | each line placed on a p53-output axis |
| `mg53_p53/findings/tables/tp53_mutation_annotation.csv` | per-variant annotation |
| `mg53_p53/findings/tables/null_reference_lines.csv` | the zero-p53-output anchor lines |
| `mg53_p53/findings/tables/p53_nullification.csv` | how far p53 is disabled across the panel |

## MDM2 against MG53

| Table | What it holds |
|---|---|
| `mg53_p53/findings/tables/mdm2_mg53_bins.csv` | every binned level comparison |
| `mg53_p53/findings/tables/mdm2_mg53_cpm_by_plate.csv` | the plate decomposition that explains the one large number |
| `mg53_p53/findings/tables/mdm2_mg53_single_cell.csv` | MG53-positive against MG53-negative cells of the same well |
| `mg53_p53/findings/tables/mdm2_mg53_genotype_interaction.csv` | the interaction that is p 2e-06 raw and p 0.36 within exposure |
| `mg53_p53/findings/tables/mdm2_mg53_allgene_null.csv` | MDM2's percentile in each reference family |

## The measurement with controls

| Table | What it holds |
|---|---|
| `mg53_p53/findings/tables/mg53_to_p53_effect.csv` | p53 activity change per MG53 change, by arm, with the p53-null control |

## The run's own output

The nine pipeline steps each write a `tables/` folder; the committed copies in `mg53_p53/*/tables/` are the **regression reference** a fresh run compares itself against. `mg53_p53/export/` writes the machine-readable extract the findings are built from.
